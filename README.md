# Temporary File Remover

### Requirements

1. Windows 7 or higher.
2. Make sure you have installed Python in your computer.
3. `pip` vrsion: 19.0 or higher and then `pip install win10toast`
4. Make sure you have added Python paths in Environment Variable path.

### Setup

To add this program to startup programs, open your registry with **Windows key** + **R** and find the following key: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` and then right click on your mouse and create a new string value using a descriptive name, and set the value of the string to the path of [runner.vbs](runner.vbs) then press **OK** and restart your computer. After restarting your computer you will see the program is running in background.

### How does it works

Temporary File Remover deletes your temporary files from `C:\Windows\Temp`, `C:\Windows\Prefetch` and `C:\Users\<USERNAME>\AppData\Local\Temp` from your computer. It starts at startup and runs in the background. Once it runs, it takes 2 hours of break and then runs again and notifies you that it is running.

## Note

In [app.py](app.py), please `<USERNAME>` by your user name:
```python
path_temp2 = 'C:\\Users\\<USERNAME>\\AppData\\Local\\Temp'
```

And enter the correct file location where the files you downloaded in [runner.vbs](runner.vbs) and [runner.bat](runner.bat).  
runner.vbs
```vbs
CreateObject("Wscript.Shell").Run "PATH\TO\DIR\runner.vbs", 0, True
```
runner.bat
```bat
python PATH\TO\DIR\app.py
```
