"""
Purpose: Watch and compile C++
Date created: 2020-07-09

Contributor(s):
    Mark M.
"""


import os
import re
import sys
import platform
import shlex
import msvcrt    # Windows-specific functions.
import subprocess
from time import sleep
import concurrent.futures as ccf
from subprocess import PIPE, STDOUT, Popen,TimeoutExpired

CPP_FOLDER = r"C:\path\to\cpp\folder"


def set_dir(folder_path=None):
	"""Change directories (useful for testing.)"""
	
    isdir_ = os.path.isdir
    normpath_ = os.path.normpath

    if folder_path is None:
        return normpath_(os.getcwd())
    elif isdir_(folder_path):
        return normpath_(folder_path)


c_cpp_dir = set_dir(CPP_FOLDER)


### C++ compiler options.
# This is very, very rough and only useful for MinGW on Windows.

COMPILER = "g++"
WARNING_OPTS = ["Wall", "Wextra"]
OTHER_OPTS = []
EXE_NAME = "abc123"
# exe_name = f"{EXE_NAME}.exe"


def create_cmd(filepath, exe_name=EXE_NAME):
	"""Generate a C++ compilation command."""
	
    args = " ".join(map(lambda x: f"-{x}", WARNING_OPTS + OTHER_OPTS))
    if " " in filepath:
        return f'{COMPILER} {args} -o {exe_name} "{filepath}"'
    else:
        return f'{COMPILER} {args} -o {exe_name} {filepath}'



# Regular expression pattern to find C/C++ file extensions.
C_EXTENSIONS_PATTERN = r"^.+\.(h|c|C){1,2}([xp\+]{0,2})?$"


def get_local_files(top_level_folder, re_pattern=C_EXTENSIONS_PATTERN, relative_paths=False):
	"""Will walk a directory and gather all C/C++ files, including headers."""
	
    p = re.compile(re_pattern)
    f_list = []
    for root, subdirs, files in os.walk(top_level_folder):
        for d in subdirs:
            if str(d).startswith("."):
                subdirs.remove(d)
        for f in files:
            res = p.search(f)
            if res:
                if relative_paths:
                    if os.path.relpath(root) != ".":
                        f_list.append(os.path.join(os.path.relpath(root), f))
                    else:
                        f_list.append(f)
                else:
                     f_list.append(os.path.join(root, f))
    return f_list

# # Full paths to c/c++files
# c_files = get_local_files(c_cpp_dir)

# Relative paths to c/c++files
# Changes directories and reverts back to prior
# Mostly useful for testing/debugging, otherwise
# you should probably stick to the directory with the
# files you plan on using if using relative paths.

current_dir = os.getcwd()
os.chdir(c_cpp_dir)
c_files = get_local_files(c_cpp_dir, relative_paths=True)
os.chdir(current_dir)


# ### Concurrent Futuring

# Exception abstraction.
class ConcurrentException(Exception):
    pass

class FutureDataError(ConcurrentException):
    pass


def run_task(command, to_seconds=15):
	"""Function to execute subprocess for a given command.
	
	:param to_seconds: Seconds for process to wait before timing out.
	"""
	
    outs, errs = None, None
    proc = subprocess.Popen(command,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE
                            )
    try:
        outs, errs = proc.communicate(timeout=to_seconds)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    return outs, errs


def run_commands(commands):
	"""Driver function to concurrently run commands.  The major aspect of this 
	is running multiple files and wanting to see the output of compiled files
	while working on them.
	"""
    n_workers = (len(commands) + 1) // 2 if len(commands) <= 61 else 61

    with ccf.ThreadPoolExecutor(max_workers=n_workers) as executor:
        cmd_futures = {executor.submit(run_task, cmd, 15):str(i) for i, cmd in enumerate(commands)}
        for task in ccf.as_completed(cmd_futures):
            cmd_index = cmd_futures[task]
            try:
                o, e = task.result()
                bmsg = b"\n".join([o, e])
                print(bmsg)
            except FutureDataError:
                pass
				
				
if __name__ == "__main__":
	"""Run our program.
	
	I don't know what DEBUG = False will do, yet.  Nothing
	good, I'm sure of it.
	"""
	#TODO: Allow for command prompt not to require focus before detecting keystrokes.
	
	DEBUG = True
	
	if DEBUG:
    	test_file = "<my-test-script>.cpp"
	
	# Compile the executable afterwards?
    check_output = False

    print(f"Watching folder / script {c_cpp_dir} for changes...")

    while True:
	
        # ### Listen for CTRL + C; Fire evaluator if detected.
        wchar = msvcrt.getwch()
        o_wchar = ord(wchar)
		
        if o_wchar == 19: # If `CTRL + S` key combo detected
			# Create a compilation string
            cmd_string = create_cmd(test_file)

			# Set command list to generated string.
            cmd_list = [cmd_string,]

			# If we want to run the executable, this will append that command.
            if check_output:
                cmd_list.append([f"cmd.exe /c {EXE_NAME}"])
			
			# Run our threading process to compile our scripts.
            run_commands(cmd_list)
