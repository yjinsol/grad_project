import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
omniboxHwnd = win32gui.FindWindowEx(hwnd,0,'Chrome_OmniboxView', None)


def _decode(buff):
    return buff.decode('utf-8').strip('\0')

def getWindowText(hwnd):
    buf_size = 1 + win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
    buf = win32gui.PyMakeBuffer(buf_size)
    win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, buf_size, buf)
    #return str(buf)
    return _decode(buf.tobytes())

print(getWindowText(hwnd))