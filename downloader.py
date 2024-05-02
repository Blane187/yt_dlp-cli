import os
import argparse
import yt_dlp

def downloader(url, save_path, audio_format, audio_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
        }],
        'outtmpl': save_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Audio Downloader")
    parser.add_argument("url", "video_url", help="URL of the YouTube video")
    parser.add_argument("sv_fl", "save_folder", help="Folder path to save the downloaded audio")
    parser.add_argument("ad_fr", "audio_format", help="Preferred audio format (e.g., mp3, m4a)")
    parser.add_argument("name_ad", "audio_name", help="Name for the downloaded audio file")

    args = parser.parse_args()

    save_path = os.path.join(args.save_folder, args.audio_name)
    downloader(args.video_url, save_path, args.audio_format, args.audio_name)
    print("Download Complete!")
