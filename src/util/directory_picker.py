import tkinter as tk
from tkinter import filedialog

def directory_picker(self):
    itself = self
    path = filedialog.askdirectory()
    if path:
        itself.path_var.set(path)