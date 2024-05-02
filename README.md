# yt_dlp-cli


This script allows you to download audio from YouTube videos in your preferred format.

## Prerequisites
- Python 3
- `yt-dlp` library (install via `pip install yt-dlp`)

## Usage
1. Run the script with the following command:
    ```
    python downloader.py <video_url> <save_folder> <audio_format> <audio_name>
    ```
| Flag                                       | Description |
|--------------------------------------------|-------------|
| `-h`, `--help`                             | Show this help message and exit. |
| `video_url`                                  | URL of the YouTube video. |
| `save_folder`                                 | Folder path to save the downloaded audio. |
| `audio_format`             
  | Preferred audio format (e.g., mp3, m4a).|
| `--audio_name`
| Name for the downloaded audio file.
|
``
    

2. After running the command, the script will download the audio from the specified YouTube video and save it to the specified folder with the specified name.

3. Once the download is complete, a message will be displayed confirming the completion.

## Example
```
python downloader.py https://www.youtube.com/watch?v=video_id /path/to/save mp3 my_audio
```

This will download the audio from the YouTube video with the specified ID (`video_id`), save it as `my_audio.mp3` in the `/path/to/save` folder.

--- 

Feel free to expand or modify this README as needed!
