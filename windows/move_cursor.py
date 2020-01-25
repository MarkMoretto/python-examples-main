
"""
Purpose: 
Date created: 2020-01-25

Contributor(s):
    Mark M.
"""

import os
import re
from math import cos, sin
from time import sleep
import ctypes as C
from ctypes import wintypes


char_ptr = C.POINTER(C.c_char)
wchar_ptr = C.POINTER(C.c_wchar)

k32 = C.WinDLL("kernel32", use_last_error=True)
user32 = C.WinDLL("user32", use_last_error=True)


user32.SetCursorPos.argtypes = [wintypes.INT, wintypes.INT]
user32.SetCursorPos.restype = wintypes.BOOL

def move_cursor_to_point(x, y):
    res = user32.SetCursorPos(x, y)
    if res == 0:
        print("Error moving cursor.")

### Move cursor in spiral
def move_cursor_in_spiral(n_seconds = 10):

    n_points = int(n_seconds / 0.05)
    for i in range(n_points):
        x = int(500 + cos(i / 5) * i)
        y = int(500 + sin(i / 5) * i)
        user32.SetCursorPos(x, y)
        sleep(0.05)


move_cursor_in_spiral(5)


### Create some input and location structures
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input

#-- Static variables
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

def process_struct(input_str):

    header_pat = r"typedef\sstruct\s(\w+)\s+{"
    struct_header = [i.strip() for i in input_str.strip().split('\n') \
                     if i.startswith(('typedef',))]
    class_name = re.search(header_pat, struct_header[0]).group(1)

    struct_tokens = [i.strip() for i in input_str.strip().split('\n') \
                     if not i.startswith(('typedef','}',))]
    struct_wintypes = [re.split(r"\s+", i)[0] for i in struct_tokens]
    struct_fields = [re.split(r"\s+", i)[1].replace(';','') for i in  struct_tokens]

    output = f"class {class_name}(C.Structure):\n\t_fields_ = [\n"
    frmt_list = [f'\t\t("{i[1]}", wintypes.{i[0]})' for i \
                 in list(zip(struct_wintypes, struct_fields))]
    output += ',\n'.join(frmt_list) + "\n\t\t]"

    print(output)

struct_string ="""
typedef struct tagHARDWAREINPUT {
  DWORD uMsg;
  WORD  wParamL;
  WORD  wParamH;
} HARDWAREINPUT, *PHARDWAREINPUT, *LPHARDWAREINPUT;
"""

# process_struct(struct_string)


class MOUSEINPUT(C.Structure):
    _fields_ = [
                ("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", C.POINTER(wintypes.ULONG))
                ]

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-keybd_event
class KEYBDINPUT(C.Structure):
    _fields_ = [
                ("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", C.POINTER(wintypes.ULONG))
                ]


class HARDWAREINPUT(C.Structure):
    _fields_ = [
                ("uMsg", wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD)
                ]


class INPUTUNION(C.Structure):
    _fields_ = [
               ("mi", MOUSEINPUT),
               ("ki", KEYBDINPUT),
               ("hi", HARDWAREINPUT),
            ]


class INPUT(C.Structure):
    _fields_ = [
            ("type", wintypes.DWORD),
            ("value", INPUTUNION),
            ]


### Type something with the keyboard
KEYEVENTF_KEYUP = 0x0002

def kpress(vk, down):
    inputs = INPUT(
            type = INPUT_KEYBOARD,
            value = INPUTUNION(
                    ki=KEYBDINPUT(
                        wVk=vk,
                        wScan=0,
                        dwFlags=0 if down else KEYEVENTF_KEYUP,
                        time=0,
                        dwExtraInfo=None
                    )
                )
            )
    user32.SendInput(1, C.byref(inputs), C.sizeof(inputs))

test_str = 'HELLO'

sleep(2)
for ch in test_str:
    kpress(ord(ch), down=True)
    kpress(ord(ch), down=False)



### Mouse action
class POINT(C.Structure):
    _fields_ = [
            ("x", wintypes.LONG),
            ("y", wintypes.LONG),
            ]



def get_mouse():
    point = POINT()
    user32.GetCursorPos(C.byref(point))
    return point.x, point.y


# Press CTRL + C to stop
try:
    while True:
        print(get_mouse())
        sleep(0.05)
except KeyboardInterrupt:
    print('Keypress detected!')









