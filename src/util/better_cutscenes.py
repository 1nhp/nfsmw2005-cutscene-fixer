import threading
import urllib.request
from zipfile import ZipFile
import sys
from modules import *
import time
import os

# Progress bar function
def progress_bar(self, downloaded, total):
    if total > 0: 
        percent = downloaded * 100 / total
        self.set(f"\rStatus: Downloading archive: {percent:.1f}%")

# Download MOVIES.zip file
def download(self, url=xbox360_cutscenes_download_url_gdrive):
    def task():
        file_name = path + "Movies.zip"
        last_update = 0

        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                size = int(response.getheader("Content-Length", 0))
                downloaded = 0 

                with open(file_name, "wb") as f:
                    while True:
                        chunk = response.read(8192)
                        f.write(chunk)
                        if not chunk:
                            break 
                        downloaded += len(chunk)

                        # Update the progress bar every 0.1 seconds
                        # to prevent cpu usage
                        now = time.time()
                        if now - last_update > 0.1:
                            progress_bar(self, downloaded, size)
                            last_update = now
            install(self)

        except Exception as e:
            self.set(f"error occurred: {e}")

    # Run the download in a separate thread
    threading.Thread(target=task, daemon=True).start()

# Extracts the zip file that has the MOVIES folder
def install(self):
    with ZipFile(path + "MOVIES.zip", "r") as archive:
        self.set("Status: Extracting...")
        archive.extractall(path=path)
        self.set("Status: Installed Xbox 360 cutscenes succesfully!")