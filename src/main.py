from tkinter import *
from tkinter import ttk
from variables import *
from directory_picker import directory_picker
from rename_files import rename_files
from help_window import about
from center_window import center_window
from tktooltip import ToolTip

class App:
    def __init__(self, root):
        self.root = root

        # Window configuration
        root.title("NFSMW2005 Cutscene Fixer")
        window = center_window(root, 520, 120)
        root.geometry(window)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1) 

        #root.resizable(False, False)
        menubar = Menu(root)

        style = ttk.Style(root)
        style.theme_use("vista")

        # Default path
        self.path_var = StringVar(value=path)

        # Container
        container = ttk.Frame(root, padding=10)
        container.grid(sticky=NSEW)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=1) 


        # Main frame
        main_frame = ttk.Frame(container)
        main_frame.grid(sticky=NSEW)
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=0)

        # Path label
        path_label = ttk.Label(main_frame, text="Movies path")
        path_label.grid(sticky=NSEW)

        # Path entry
        self.path_entry = ttk.Entry(main_frame, textvariable=self.path_var)
        self.path_entry.grid(column=1, row=0, sticky=NSEW)
        
        self.status = StringVar(value="Status: None")

        # Directory button
        path_dir_button = ttk.Button(main_frame,text="Choose directory", command=lambda: directory_picker(self))
        path_dir_button.grid(column=2, row=0, padx=3, sticky=NSEW)

        # Fix buttons frame
        fix_buttons_frame = ttk.Frame(main_frame)
        fix_buttons_frame.grid(column=1, row=1, pady=5, sticky=NSEW)
        fix_buttons_frame.columnconfigure(0, weight=1)
        fix_buttons_frame.columnconfigure(1, weight=1)

        # The fix buttons themselves
        # NTSC
        fix_button_ntsc = ttk.Button(fix_buttons_frame, text="Fix cutscenes (English)", command=lambda: rename_files("pal", "ntsc", self.status))
        fix_button_ntsc.grid(column=0, row=1, sticky=NSEW)
        ToolTip(fix_button_ntsc, msg="Renames the cutscene files from tollbooth_tutorial_english_pal.vp6 to tollbooth_tutorial_english_ntsc.vp6, ONLY works if copy is using english cutscene filenames")

        # PAL 
        fix_button_pal = ttk.Button(fix_buttons_frame, text="Fix cutscenes (Europe)", command=lambda: rename_files("ntsc", "pal", self.status))
        fix_button_pal.grid(column=1, row=1, sticky=NSEW)
        ToolTip(fix_button_pal, msg="Renames the cutscene files from tollbooth_tutorial_english_ntsc.vp6 to tollbooth_tutorial_english_pal.vp6, ONLY works if copy is using european cutscene filenames")

        # Status frame
        status_frame = ttk.Frame(container)
        status_frame.grid(pady=5, column=0, row=2)

        # The progress label
        progress_label = ttk.Label(status_frame, textvariable=self.status)
        progress_label.grid(column=0, row=2, sticky=NSEW)

        # Top menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=about)

        menubar.add_cascade(label="Help", menu=help_menu)
        root.config(menu=menubar) 

# Start program
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()