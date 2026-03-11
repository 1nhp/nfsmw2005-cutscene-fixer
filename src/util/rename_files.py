import os
import re
from variables import path

def rename_files(old_substring, new_substring, self):
    self.set("Status: Renaming...")  
    folder = path
    renamed_any = False 

    # Check if folder exists
    if not os.path.isdir(folder):
        self.set("Status: ERR - Folder not found!")
        return

    self.set("Status: Renaming...")
    renamed_any = False 

    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)

        # Skip directories
        if not os.path.isfile(old_path):
            continue

        # Check if the filename contains the target substring
        if old_substring.lower() in filename.lower():
            new_filename = re.sub(old_substring, new_substring, filename, flags=re.IGNORECASE)
            new_path = os.path.join(folder, new_filename)

            # Safety check: skip if the new filename already exists
            if os.path.exists(new_path):
                continue

            os.rename(old_path, new_path)
            renamed_any = True

    if renamed_any:
        self.set("Status: Renamed files successfully!")
    else:
        self.set("Status: ERR - No filenames matched!")
