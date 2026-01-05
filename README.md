# Spotify Playlist Archiver & Sanitizer

A robust Python automation tool designed to ingest Spotify playlists and convert them into high-fidelity MP3s (320kbps CBR). This tool is specifically engineered to optimize audio files for legacy hardware, embedded systems, and car stereos by performing intelligent filename sanitization and metadata handling.

## 🚀 Overview

Modern audio players handle special characters and emojis without issues, but legacy hardware (such as car head units from 2010-2018) often fails to read files with non-ASCII characters or complex directory structures. 

This project solves that interoperability problem by implementing a pipeline that:
1.  **Downloads** audio tracks using the `spotdl` engine.
2.  **Forces** high-quality encoding (320kbps MP3).
3.  **Sanitizes** filenames via Regex to ensure 100% ASCII compatibility.
4.  **Maintains** a download history to prevent duplication during batch operations.

## ✨ Key Features

* **High-Fidelity Audio:** Enforces 320kbps Constant Bit Rate (CBR) MP3 encoding for maximum audio quality.
* **Legacy Hardware Compatibility:** Automatically strips emojis, special characters, and diacritics (e.g., `ñ`, `á`, `🔥`) from filenames to prevent read errors on older file systems (FAT32).
* **Smart Idempotency:** Uses a local `download_history.txt` manifest to track downloaded tracks. Re-running a playlist will skip already processed songs, saving bandwidth and time.
* **Batch Processing:** The application runs in a continuous loop, allowing the user to queue multiple playlists in a single session.
* **Flat Architecture:** Outputs files into a single directory to ensure compatibility with players that struggle with nested folder structures.

## 🛠️ Tech Stack

* **Python 3.12+**
* **SpotDL:** For Spotify metadata extraction and YouTube Music audio source retrieval.
* **FFmpeg:** For audio transcoding and normalization.
* **Regex:** For string pattern matching and filename sanitization.

## ⚙️ Installation

### Prerequisites
* Python 3.12 or higher.
* **FFmpeg** installed and added to your system PATH.

### Setup

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/spotify-archiver.git](https://github.com/your-username/spotify-archiver.git)
    cd spotify-archiver
    ```

2.  Create and activate a virtual environment:
    ```bash
    # Windows (Git Bash)
    python -m venv venv
    source venv/Scripts/activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install spotdl
    ```

## 💻 Usage

1.  Run the main script:
    ```bash
    python main.py
    ```

2.  Paste a **public** Spotify Playlist URL when prompted.
3.  The tool will begin downloading and processing files into the `./audio` directory.
4.  To stop the program, type `exit` or press `Ctrl+C`.

## ⚠️ Disclaimer

This tool is for **educational and personal archiving purposes only**. It relies on third-party libraries (`spotdl`) to fetch content from YouTube Music. The user is responsible for respecting copyright laws and the Terms of Service of the respective platforms. The developer of this repository does not host any copyrighted files.

---
*Built with Python 3.12*
