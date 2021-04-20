# Temporary File Remover

### Requirements

1. Windows OS
2. Make sure you have correctly installed Python in your computer.
3. Minimum pip vrsion:19.0.
4. Make sure you have added Python paths in Environment Variable path.
5. Open The terminal and install - `pip install win10toast`

### Setup

To start this program automatically at startup open your registry with `Windows key + R` and find the following key: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` and then right click on your mouse and create a new string value using a descriptive name, and set the value of the string to the path of [runner.vbs](runner.vbs) then press ok and restart your computer. After restarting your computer you will see the program is running in the background.

### How does it works

Temporary File Remover deletes your temporary files(Temp, Prefetch) from your computer(Only for windows). It starts at startup and runs in the background. Once it runs, it runs again after 2 hours and notifies you that its running.

## Note

In [app.py](app.py), please cut the curly braces enter your Username:
```python
path_temp2 = 'C:\\Users\\{Username}\\AppData\\Local\\Temp'
```

And enter the correct file location where the files you downloaded in [runner.vbs](runner.vbs) and [runner.bat](runner.bat).  
runner.vbs
```vbs
CreateObject("Wscript.Shell").Run "{Path}\runner.vbs", 0, True
```
runner.bat
```bat
python {Path}\app.py
```
