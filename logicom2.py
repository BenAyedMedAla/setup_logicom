import os
import subprocess
import mysql.connector
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, font
import winshell

def find_directory(directory_name):
    drives = ['D:', 'E:', 'F:', 'G:', 'H:','C:']  

    # Search for the directory in the specified drives
    for drive in drives:
        directory_path = os.path.join(drive, directory_name)
        if os.path.exists(directory_path):
            return directory_path
        
def select_destination():
    destination = filedialog.askdirectory()
    if destination:
        move_folder(destination)

def move_folder(destination):
    source_folder = find_directory("installation/ERP LOGICOM")
    folder_name = os.path.basename(source_folder)
    destination_folder = os.path.join(destination, folder_name)

    try:
        shutil.move(source_folder, destination_folder)
        create_shortcut(destination_folder)
        messagebox.showinfo("Success", f"Folder moved to {destination_folder}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_shortcut(folder_path):
    desktop = winshell.desktop()
    target = os.path.join(folder_path, 'PRJGCOM.exe')
    shortcut_path = os.path.join(desktop, 'PRJGCOM.lnk')
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = target
        shortcut.description = "Shortcut to PRJGCOM"
        shortcut.working_directory = folder_path
    messagebox.showinfo("Success", "Shortcut created on desktop")

def submit_info():
    global societe_name,societe_code
    societe_name = societe_name_var.get()
    societe_code = societe_code_var.get()
    # You can use societe_name and societe_code variables in your script as needed
    messagebox.showinfo("Info Submitted", f"Nom de societé: {societe_name}\nCode de societé: {societe_code}")
    root.destroy()  # Close the interface

# Set up the main GUI window
root = tk.Tk()
root.title("Move ERP LOGICOM Folder")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Create a frame for the canvas and scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create a canvas widget
canvas = tk.Canvas(frame, bg="#f0f0f0")
canvas.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the content
content_frame = tk.Frame(canvas, bg="#f0f0f0")
content_frame.pack(expand=True, pady=20)  # Add padding to center content vertically
canvas.create_window((canvas.winfo_width() / 2, 0), window=content_frame, anchor="n")

# Set up fonts
title_font = font.Font(family="Helvetica", size=18, weight="bold")
text_font = font.Font(family="Helvetica", size=12)

# Add a title label
title_label = tk.Label(content_frame, text="Move ERP LOGICOM Folder", font=title_font, bg="#f0f0f0")
title_label.pack(pady=20)

# Add an instruction label
instruction_label = tk.Label(content_frame, text="Click the button below to select the destination folder for 'ERP LOGICOM'.", font=text_font, bg="#f0f0f0", wraplength=400)
instruction_label.pack(pady=10)

# Add a button to select the destination folder
move_button = tk.Button(content_frame, text="Select Destination", font=text_font, command=select_destination, bg="#4CAF50", fg="white", padx=10, pady=5)
move_button.pack(pady=20)

# Add a label to show the current source folder
source_label = tk.Label(content_frame, text=f"Current folder: installation/ERP LOGICOM", font=text_font, bg="#f0f0f0")
source_label.pack(pady=10)

# Add fields for 'nom de societé' and 'code de societé'
societe_name_var = tk.StringVar()
societe_code_var = tk.StringVar()

societe_name_label = tk.Label(content_frame, text="Nom de societé:", font=text_font, bg="#f0f0f0")
societe_name_label.pack(pady=5)
societe_name_entry = tk.Entry(content_frame, textvariable=societe_name_var, font=text_font)
societe_name_entry.pack(pady=5)

societe_code_label = tk.Label(content_frame, text="Code de societé:", font=text_font, bg="#f0f0f0")
societe_code_label.pack(pady=5)
societe_code_entry = tk.Entry(content_frame, textvariable=societe_code_var, font=text_font)
societe_code_entry.pack(pady=5)

# Add a button to submit the 'nom de societé' and 'code de societé'
submit_button = tk.Button(content_frame, text="Submit Info", font=text_font, command=submit_info, bg="#4CAF50", fg="white", padx=10, pady=5)
submit_button.pack(pady=20)

root.mainloop()

# Renaming the folder after the Tkinter interface closes
base_path =find_directory("installation/DATA")
demo_folder_path = os.path.join(base_path, 'Demo')
new_folder_path = os.path.join(base_path, societe_code)

if os.path.exists(demo_folder_path):
    try:
        os.rename(demo_folder_path, new_folder_path)
        print(f"Folder renamed to {societe_code}")
    except Exception as e:
        print(f"Error renaming folder: {e}")
else:
    print("The folder 'DEMO' does not exist.")

if os.path.exists(r"D:/EasyPHP-12.1/mysql/data"):
    base_target_path = 'D:/EasyPHP-12.1/mysql/data'
else:
    base_target_path = 'C:/EasyPHP-12.1/mysql/data'


folders_to_move = [
        os.path.join(base_path, 'BDVIDEERP'),
        os.path.join(base_path, 'userERPvide'),
        os.path.join(base_path, 'USERERP'),
        new_folder_path
    ]
for folder in folders_to_move:
        folder_name = os.path.basename(folder)
        new_folder_path = os.path.join(base_target_path, folder_name)
        
        if os.path.exists(folder):
            try:
                shutil.move(folder, new_folder_path)
                print(f"Moved {folder} to {new_folder_path}")
            except Exception as e:
                print(f"Error moving folder {folder}: {e}")
        else:
            print(f"Folder {folder} does not exist.")

try:
    conn = mysql.connector.connect(
        host="localhost",   # or your MySQL server host
        user="root",
        password="",
        database="usererp"
    )
    cursor = conn.cursor()

    # Update the `code` and `rsoc` columns in the `societe` table
    update_query = """
    UPDATE societe
    SET code = %s, rsoc = %s
    where code="DEMO"
    """
    cursor.execute(update_query, (societe_code, societe_name))

    update_query1 = """
    UPDATE usermodule
    SET societe = %s
    where societe="DEMO"
    """
    cursor.execute(update_query1, (societe_code))

    update_query2 = """
    UPDATE usermoduleprtmp
    SET societe = %s
    where societe="DEMO"
    """
    cursor.execute(update_query2, (societe_code))

    update_query3 = """
    UPDATE usermodulepr
    SET societe = %s
    where societe="DEMO"
    """
    cursor.execute(update_query3, (societe_code))

    update_query4 = """
    UPDATE dernutil
    SET societe = %s, chemin= %s
    where societe="DEMO"
    """
    cursor.execute(update_query4, (societe_code,societe_code))

    update_query5 = """
    UPDATE paramaitre
    SET  code= %s
    where code="DEMO"
    """
    cursor.execute(update_query5, (societe_code))

    update_query6 = """
    UPDATE paramstock
    SET  code= %s
    where code="DEMO"
    """
    cursor.execute(update_query6, (societe_code))

    update_query7 = """
    UPDATE usermoduletmp
    SET societe = %s
    where societe="DEMO"
    """
    cursor.execute(update_query7, (societe_code))

    update_query8 = """
    UPDATE usersoc
    SET societe = %s, rsoc = %s
    where societe="DEMO"
    """
    cursor.execute(update_query8, (societe_code, societe_name))

    update_query9 = """
    UPDATE usersoctmp
    SET societe = %s
    where societe="DEMO"
    """
    cursor.execute(update_query9, (societe_code))

    conn.commit()
    print("Successfully updated all necessary tables.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()