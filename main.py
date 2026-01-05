import os
import subprocess
import re
from pathlib import Path

class SpotifyDownloader:
    def __init__(self, output_folder="audio"):
        self.base_dir = Path(os.getcwd()) / output_folder
        self.archive_file = Path(os.getcwd()) / "download_history.txt"
        self.spotdl_bin = "spotdl" 
        
        self.base_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INIT] Working directory: {self.base_dir}")

    def download_playlist(self, spotify_url):
        print(f"\n[INFO] Starting download process for: {spotify_url}")

        output_template = str(self.base_dir / "{artist} - {title}")

        command = [
            self.spotdl_bin,
            "download",
            spotify_url,
            "--format", "mp3",
            "--bitrate", "320k",
            "--output", output_template,
            "--overwrite", "skip",
            "--archive", str(self.archive_file)
        ]

        try:
            subprocess.run(command, check=True)
            print("\n[SUCCESS] Download completed.")
        except subprocess.CalledProcessError as e:
            print(f"\n[ERROR] Download failed with exit code: {e.returncode}")
        except FileNotFoundError:
            print("\n[CRITICAL] 'spotdl' executable not found. Ensure it is installed in your environment.")

    def sanitize_filenames(self):
        print(f"\n[INFO] Sanitizing filenames...")
        
        count = 0
        for file_path in self.base_dir.glob("*.mp3"):
            original_name = file_path.name
            
            clean_name = original_name
            replacements = {
                'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
                'ñ': 'n', 'Ñ': 'N', 'ü': 'u'
            }
            for char, rep in replacements.items():
                clean_name = clean_name.replace(char, rep)

            clean_name = re.sub(r'[^\w\s\-\.]', '', clean_name)
            clean_name = re.sub(r'\s+', ' ', clean_name).strip()

            if clean_name != original_name:
                new_path = self.base_dir / clean_name
                try:
                    file_path.rename(new_path)
                    count += 1
                except OSError as e:
                    print(f"[WARN] Could not rename {original_name}: {e}")

        print(f"[INFO] Post-processing finished. {count} files renamed.")
        print(f"[DONE] Files available at: {self.base_dir}")

if __name__ == "__main__":
    downloader = SpotifyDownloader(output_folder="audio")
    
    print("--- Spotify Batch Downloader ---")
    print("Files will accumulate in the 'audio' folder.")
    print("Type 'exit' to close the program.\n")

    while True:
        try:
            url = input(">>> Enter Spotify Playlist URL: ").strip()
            
            if url.lower() in ['exit', 'quit']:
                print("[EXIT] Closing application.")
                break

            if "spotify.com" in url:
                downloader.download_playlist(url)
                downloader.sanitize_filenames()
                print("\n[READY] Playlist processed. Ready for the next one.")
            elif url == "":
                continue
            else:
                print("[ERROR] Invalid Spotify URL.")
                
        except KeyboardInterrupt:
            print("\n[EXIT] Operation cancelled by user.")
            break