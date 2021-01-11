
"""
Purpose: Unlink and remove a .git folder in a local repo
Date created: 2019-04-16
Contributor(s): Mark Moretto

Ref: https://stackoverflow.com/questions/55717798/how-to-delete-directory-with-git-folder-in-python/55718140#55718140
Method ref: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
"""


import os
import stat
import shutil
from subprocess import call

dir = r'C:\Users\...\...\...'


# Borrowed from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        if op_sys.lower() == 'windows':
            while True:
                call(['attrib', '-H', tmp])
                break
            shutil.rmtree(tmp, onerror=on_rm_error)


    


