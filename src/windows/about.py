from modules import *

def about():
    root = Tk()
    window = center_window(root, about_window_size["width"], about_window_size["height"])
    root.geometry(window)    
    root.resizable(False, False)
    root.title(about_title)

    main_frame = ttk.Frame(root)
    main_frame.grid(padx=10, pady=60)

    # Label parent should be main_frame
    label = ttk.Label(main_frame, text=program_name, font=("Arial", 12, "bold"))
    copyright_label = ttk.Label(main_frame, text="© 2026-2026 Maritosu") 
    technology_label = ttk.Label(main_frame, text="Built with Python, Tkinter")

    label.grid(row=0, column=0)  # specify row/column
    copyright_label.grid(row=1, column=0)  # specify row/column
    technology_label.grid(pady=10, row=2, column=0)

    root.mainloop()