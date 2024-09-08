import os,time
import sys
import pyautogui
import mysql.connector
import ctypes,subprocess
from pywinauto import *
from pywinauto.keyboard import send_keys
import pyuac
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox,filedialog, font
import shutil
import winshell

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:])
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit()

if not is_admin():
    print("Not running as Administrator. Restarting with elevated privileges...")
    restart_as_admin()

test=False
def get_credentials():
    def submit():
        username = username_entry.get()
        password = password_entry.get()
        if username == "test" and password == "test":
            root.quit()
            root.destroy()
            test=True
        else:
            messagebox.showwarning("Input Error", "Please enter the correct username and password")

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.quit()
            root.destroy()

    root = tk.Tk()
    root.title("Authentification")
    root.geometry("600x300")
    root.configure(bg="lightblue")

    tk.Label(root, text="Username:", bg="lightblue").pack(pady=10)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:", bg="lightblue").pack(pady=10)
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=submit, bg="green", fg="white")
    submit_button.pack(pady=20)

    quit_button = tk.Button(root, text="Quit", command=on_closing, bg="red", fg="white")
    quit_button.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

get_credentials()

def find_directory(directory_name):
    drives = ['D:', 'E:', 'F:', 'G:', 'H:','C:']  

    # Search for the directory in the specified drives
    for drive in drives:
        directory_path = os.path.join(drive, directory_name)
        if os.path.exists(directory_path):
            return directory_path

def find_installer(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def install_easyphp(installer_path):
     
    if os.path.exists(installer_path):
            if not pyuac.isUserAdmin():
                pyuac.runAsAdmin()
            else:
                app=Application(backend='uia').start(installer_path)
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{TAB}")
                send_keys("{UP}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                if os.path.exists('D:'):
                    send_keys("D:\EasyPHP-12.1")
                else:
                    send_keys("C:\EasyPHP-12.1")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(20)
                send_keys("{ENTER}")
    else:
        print(f"Le fichier {installer_path} n'existe pas.")

directory=find_directory(r"installation\OUTILS LOGICOM")
print(directory)
filename = "EasyPHP-12.1_with_PHP-5.4.6-setup.exe"
installer_path = find_installer(directory, filename)
if installer_path:
    install_easyphp(installer_path)
else:
    print(f"{filename} n'a pas été trouvé dans le répertoire {directory}.")
time.sleep(20)
filename1 = "setup_COM.exe"
installer_path1 = find_installer(directory, filename1)
if installer_path1:
    if os.path.exists(installer_path1):
                app1=Application(backend='uia').start(installer_path1)
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(2)
                send_keys("{ENTER}")
                time.sleep(15)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{ENTER}")
                time.sleep(7)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{ENTER}")
                time.sleep(7)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{RIGHT}")
                time.sleep(1)
                send_keys("{ENTER}")
                time.sleep(7)
                send_keys("{ENTER}")
    else:
        print(f"Le fichier {installer_path1} n'existe pas.")
else:
    print(f"{filename1} n'a pas été trouvé dans le répertoire {directory}.")
time.sleep(20)

filename2 = "Setup_ODBC.exe"
installer_path2 = find_installer(directory, filename2)
if installer_path2:
    if os.path.exists(installer_path2):
                    app2=Application(backend='uia').start(installer_path2)
                    time.sleep(4)
                    target_window = 'MySQL Connector/ODBC 3.51'
                    count = 0
                    count1=0
                    while True:
                        window_title = pyautogui.getActiveWindowTitle()

                        if target_window not in window_title:
                            count += 1
                            with pyautogui.hold('alt'):
                                for _ in range(0, count):
                                    pyautogui.press('tab')
                            time.sleep(0.25)
                        elif count1==20 or 1:
                            break
                        count1=+1

                    time.sleep(1)
                    send_keys("{ENTER}")
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(20)
                    send_keys("{ENTER}")
    else:
        print(f"Le fichier {installer_path2} n'existe pas.")
else:
    print(f"{filename2} n'a pas été trouvé dans le répertoire {directory}.")

#changing the region .  and 3 

# PowerShell script content
powershell_script = """
# Set the new settings
Set-ItemProperty -Path 'HKCU:\\Control Panel\\International' -Name 'sDecimal' -Value '.'
Set-ItemProperty -Path 'HKCU:\\Control Panel\\International' -Name 'iDigits' -Value '3'

# Force the settings to update
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters
"""

# Write the PowerShell script to a file
with open("update_region_settings.ps1", "w") as file:
    file.write(powershell_script)

# Run the PowerShell script
subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "update_region_settings.ps1"])

# shutdown easyphp for cofiguration
result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
tasks = result.stdout.splitlines()

    # Filter tasks for EasyPHP processes
easyphp_processes = [task for task in tasks if 'easyphp' in task.lower()]

if not easyphp_processes:
        print("EasyPHP is not running.")
        

for process in easyphp_processes:
        # Extract the PID (it's usually the second item in the task line)
        pid = int(process.split()[1])
        # Kill the process
        os.system(f'taskkill /PID {pid} /F')

print("EasyPHP has been stopped.")

if os.path.exists(r"D:\EasyPHP-12.1\easyphp.ini"):
    easy_path = r"D:\EasyPHP-12.1\easyphp.ini"
else:
     easy_path = r"C:\EasyPHP-12.1\easyphp.ini"


# Function to update AutoStartServers value
    # Read the file
with open(easy_path, 'r') as file:
        lines = file.readlines()

    # Find and update the AutoStartServers line
for i, line in enumerate(lines):
        if line.startswith('AutoStartServers'):
            lines[i] = f'AutoStartServers={'Y'}\n'
              # Assuming there's only one AutoStartServers line
        elif line.startswith('AutoReloadConf'):
                lines[i] = f'AutoReloadConf={'N'}\n'
        elif line.startswith('AutoStartEasyPhp'):
                lines[i] = f'AutoStartEasyPhp={'Y'}\n'
        elif line.startswith('CheckVersion'):
                lines[i] = f'CheckVersion={'N'}\n'
        

    # Write the updated content back to the file
with open(easy_path, 'w') as file:
        file.writelines(lines)
# configurer mysql 
if os.path.exists(r"D:\EasyPHP-12.1\easyphp.ini"):
    myini_path = r"D:\EasyPHP-12.1\mysql\my.ini"
else:
     myini_path = r"C:\EasyPHP-12.1\mysql\my.ini"

with open(myini_path, 'r') as file:
    lines = file.readlines()
for i, line in enumerate(lines):
    if line.strip().startswith('bind-address'):
        lines[i] = f'#{line}'  # Comment out the line by adding #
        break  # Assuming there's only one bind-address line
with open(myini_path, 'w') as file:
    file.writelines(lines)
print("my.ini file updated successfully.")



# installation des dll 
time.sleep(10)
directory3=find_directory(r"installation\OUTILS LOGICOM\Package DLL INSTALLATION") 
filename3 = "setup.exe"
installer_path3 = find_installer(directory3, filename3)
if installer_path3:
    if os.path.exists(installer_path3):
                    app3=Application(backend='uia').start(installer_path3)
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(2)
                    send_keys("{ENTER}")
                    time.sleep(15)
                    send_keys("{ENTER}")
                    time.sleep(3)
                    send_keys("{ENTER}")
    else:
        print(f"Le fichier {installer_path3} n'existe pas.")
else:
    print(f"{filename3} n'a pas été trouvé dans le répertoire {directory3}.")


#2 click gestion commerciale
exe_path = os.path.join(directory, "SEC_LOGICOM_SMP_2021_ahmed.exe")
subprocess.Popen(exe_path)
time.sleep(2)
pyautogui.press('tab', presses=2)
pyautogui.press('enter', presses=2)
pyautogui.hotkey('alt', 'f4')

def display_termination_message():
    root = tk.Tk()
    root.title("Information")
    root.geometry("400x200")
    root.configure(bg="lightblue")

    message = "This app is terminated. Please open the second app 'logicom2'."
    tk.Label(root, text=message, bg="lightblue", font=("Arial", 12), wraplength=350).pack(pady=50)

    tk.Button(root, text="OK", command=root.quit, bg="green", fg="white").pack(pady=10)

    root.mainloop()

display_termination_message()






