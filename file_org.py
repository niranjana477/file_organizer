import os
import shutil
from pathlib import Path
from collections import defaultdict
import datetime
import platform
import tkinter as tk

root = tk.Tk()

root.geometry("700x700")

l1 = tk.Label(root,text = "Ent Source Path:")
l1.grid(row=0,column=0)
l2 = tk.Label(root,text = "Ent filetype-optional:")
l2.grid(row=1,column=0)

e1 = tk.Entry(root)
e1.grid(row=0,column=2,ipadx=35,ipady=6)
e2 = tk.Entry(root)
e2.grid(row=1,column=2,ipadx=35,ipady=6)

def based_on_type_all_files():
    groups = defaultdict(list)
    src = Path(e1.get())
    for file in os.listdir(src):
        f1 = Path(src)/file
        if f1.is_file():
            ext = f1.suffix.split(".")[-1]
            base = f1.stem
            abs = f1.absolute()
            groups[ext].append(abs)
    d=dict(groups)
    print(d)

    for key in d:
        new = f"{key} files"
        os.makedirs(new,exist_ok=True)
        for file in d[key]:
            shutil.move(str(file),new)
            
def move_specific():
    file_type = e2.get()
    new = f"{file_type} files"
    os.makedirs(new,exist_ok=True)
    src = Path(e1.get())
    for file in os.listdir(src):
        f1 = Path(src)/file
        if f1.is_file():
            ext = f1.suffix.split(".")[-1]
            if ext == file_type:
                shutil.move(str(f1),new)
                

def del_empty_folders():
    src = Path(e1.get())
    for f1 in os.listdir(src):
        f2 = Path(f1)
        if f2.is_dir():
            try:
                if not any(f2.iterdir()):
                    f2.rmdir()
                    print(f2)
                    print("deleted")
            except PermissionError:
                continue
                 

b1 = tk.Button(root,text="org based on type - all files",command=based_on_type_all_files,height=11)
b1.grid(row=2,column=0,padx=20,pady=70)

b2 = tk.Button(root,text = "Del empty folders",command=del_empty_folders,height=11)
b2.grid(row=2,column=1)

b3 = tk.Button(root,text = "move specific files",command = move_specific,height=11)
b3.grid(row=2,column=2)

root.mainloop()
        


