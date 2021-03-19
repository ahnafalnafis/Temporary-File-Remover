import os
import time

from win10toast import ToastNotifier


path_temp = 'C:\\Windows\\Temp' # YOU DON'T NEED TO CHANGE IT

path_temp2 = 'C:\\Users\\{}\\AppData\\Local\\Temp' # PLEASE CUT THE CURLY BRACES AND CHANGE YOUR USERNAME

pre = 'C:\\Windows\\Prefetch' # YOU DON'T NEED TO CHANGE IT


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
        if os.path.isdir(pre):
            os.removedirs(pre)
    except:
        print("Prefetch folder doesn't exist")


def notify():
    notifier = ToastNotifier()
    notifier.show_toast(title="Temp File Remover",
                        msg="Temp file removing started.", icon_path="E:\\Code\\Temp_file_remover\\cleaner.ico", duration=15)


def deletion():
    while True:
        try:
            notify()
            temp()
            temp_2()
            prefetch()
            time.sleep(60*120)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    deletion()
