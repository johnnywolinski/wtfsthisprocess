import pyautogui
import psutil
import win32gui
import win32con
import win32process
import time
import threading

def get_window_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    return title

def find_process_name(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.NoSuchProcess:
        return None

def monitor_window():
    previous_process_name = None
    while True:
        hwnd = win32gui.GetForegroundWindow()
        window_title = get_window_title(hwnd)
        process_name = find_process_name(hwnd)
        if process_name:
            if process_name != previous_process_name:
                print(f"Window Title: {window_title}")
                print(f"Process Name: {process_name}")
                previous_process_name = process_name
        time.sleep(1)

if __name__ == "__main__":
    print("Click on a window to get its process name.")
    print("Press Ctrl+C to exit.")

    # Start the window monitoring thread
    monitor_thread = threading.Thread(target=monitor_window)
    monitor_thread.daemon = True
    monitor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
