import os
import time

from win10toast import ToastNotifier

## Paths:
path_temp = 'C:\\Windows\\Temp' # DON'T CHANGE IT!!
prefetch = 'C:\\Windows\\Prefetch' # DON'T CHANGE IT!!
path_temp2 = 'C:\\Users\\<USERNAME>\\AppData\\Local\\Temp' # PLEASE REPLACE USERNAME BY YOUR USERNAME


def temp():
    try:
        if os.path.isdir(path_temp):
            os.removedirs(path_temp)
    except:
        print("Temp folder doesn't exist.")


def temp_2():
    try:
        if os.path.isdir(path_temp2):
            os.removedirs(path_temp2)
    except:
        print("Temp 2 folder doesn't exist.")


def prefetch():
    try:
        if os.path.isdir(prefetch):
            os.removedirs(prefetch)
    except:
        print("Prefetch folder doesn't exist")


def notify():
    notifier = ToastNotifier()
    notifier.show_toast(
        title="Temp File Remover",
        msg="Temp file removing started.",
        icon_path="PATH\\TO\\DIR\\cleaner.ico", # CHANGE ICON PATH
        duration=15
    )


def deletion():
    while True:
        try:
            notify()
            temp()
            temp_2()
            prefetch()
            time.sleep(60*120) # YOU CAN CHANGE INTERVAL
        except Exception as error:
            print(error)


if __name__ == '__main__':
    deletion()
