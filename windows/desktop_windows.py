
"""
Purpose: Restore window positioning after waking from sleep
Date created: 2020-01-24
https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadid
Contributor(s):
    Mark M.

user32_dll = r"C:\Windows\System32\user32.dll"
kern32_dll = r"C:\Windows\System32\kernel32.dll"
user32 = C.windll.LoadLibrary(usr32_dll)
kern32 = C.windll.LoadLibrary(kern32_dll)
"""

import re
import ctypes as C
from ctypes import wintypes


k32 = C.WinDLL("kernel32", use_last_error=True)
user32 = C.WinDLL("user32", use_last_error=True)


### Misc
k32.GetCurrentThreadId.restype = wintypes.DWORD
curr_thread = k32.GetCurrentThreadId()

user32.GetThreadDesktop.restype = wintypes.HDESK
user32.GetThreadDesktop.argtypes = [wintypes.DWORD]
hDesk = user32.GetThreadDesktop(curr_thread)

# k32.GetModuleHandleW.argtypes = [wtypes.LPCWSTR]
# k32.GetModuleHandleW.restype = wtypes.HMODULE

# hMod = k32.GetModuleHandleW("kernel32.dll")
null_ptr = C.POINTER(C.c_int)()

@C.WINFUNCTYPE(wintypes.BOOL, wintypes.LPCWSTR, wintypes.LPARAM)
def EnumWindowStationProc(a, b):
    print("foo has finished its job (%d, %d)" % (a.value, b.value))

EnumWindowStationProc = C.WINFUNCTYPE(wintypes.BOOL, wintypes.LPCWSTR, wintypes.LPARAM)
ewsp = EnumWindowStationProc()
user32.EnumWindowStationsW.argtypes = [C.POINTER(EnumWindowStationProc), wintypes.LPARAM]
user32.EnumWindowStationsW.restype = wintypes.BOOL
user32.EnumWindowStationsW(ewsp, null_ptr)


EnumDesktopWindows


### Window Information and Placement ###

struct_string ="""
typedef struct tagWINDOWPLACEMENT {
  UINT  length;
  UINT  flags;
  UINT  showCmd;
  POINT ptMinPosition;
  POINT ptMaxPosition;
  RECT  rcNormalPosition;
  RECT  rcDevice;
} WINDOWPLACEMENT;
"""

def process_struct(input_str):
    struct_tokens = [i.strip() for i in input_str.strip().split('\n') if not i.startswith(('typedef','}',))]
    struct_wintypes = [re.split(r"\s+", i)[0] for i in struct_tokens]
    struct_fields = [re.split(r"\s+", i)[1].replace(';','') for i in  struct_tokens]
    frmt_list = [f'\t\t("{i[1]}", wintypes.{i[0]})' for i in list(zip(struct_wintypes, struct_fields))]
    print(',\n'.join(frmt_list))

# process_struct(struct_string)


class WINDOWINFO(C.Structure):
    __fields__ = [
            ("cbSize", wintypes.DWORD),
            ("rcWindow", wintypes.RECT),
            ("rcClient", wintypes.RECT),
            ("dwStyle", wintypes.DWORD),
            ("dwExStyle", wintypes.DWORD),
            ("dwWindowStatus", wintypes.DWORD),
            ("cxWindowBorders", wintypes.UINT),
            ("cyWindowBorders", wintypes.UINT),
            ("atomWindowType", wintypes.ATOM),
            ("wCreatorVersion", wintypes.WORD)
            ]

windowinfo = WINDOWINFO()
ptr_windowinfo = C.pointer(windowinfo)



class WINDOWPLACEMENT(C.Structure):
    __fields__ = [
                ("length", wintypes.UINT),
                ("flags", wintypes.UINT),
                ("showCmd", wintypes.UINT),
                ("ptMinPosition", wintypes.POINT),
                ("ptMaxPosition", wintypes.POINT),
                ("rcNormalPosition", wintypes.RECT),
                ("rcDevice", wintypes.RECT)
                ]



windowplacement = WINDOWPLACEMENT()
windowplacement.length = C.sizeof(WINDOWPLACEMENT)


#--- Get window HWND
# user32.GetForegroundWindow.restype = wintypes.HWND
# focus_window = user32.GetForegroundWindow()

user32.GetDesktopWindow.restype = wintypes.HWND
hWnd = user32.GetDesktopWindow()

#--- Set pointer
# ptr_windowplacement = C.POINTER(windowplacement)


user32.GetWindowPlacement.argtypes = [wintypes.HWND, C.POINTER(WINDOWPLACEMENT)]
user32.GetWindowPlacement.restype = wintypes.BOOL

if user32.GetWindowPlacement(hWnd, windowplacement) == 0:
    print("GetWindowPlacement failed to process.")







user32.GetForegroundWindow.restype = wintypes.HWND
focus_window = user32.GetForegroundWindow()