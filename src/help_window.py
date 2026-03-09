from tkinter import *
from tkinter import ttk
from center_window import center_window

def about():
    root = Tk()
    window = center_window(root, 300, 200)
    root.geometry(window)    
    root.resizable(False, False)
    root.title("About")

    main_frame = ttk.Frame(root)
    main_frame.grid(padx=10, pady=60)

    # Label parent should be main_frame
    label = ttk.Label(main_frame, text="NFSMW2005 Cutscene Fixer", font=("Arial", 12, "bold"))
    copyright_label = ttk.Label(main_frame, text="© 2026-2026 Maritosu") 
    technology_label = ttk.Label(main_frame, text="Built with Python, Tkinter")

    label.grid(row=0, column=0)  # specify row/column
    copyright_label.grid(row=1, column=0)  # specify row/column
    technology_label.grid(pady=10, row=2, column=0)

    root.mainloop()