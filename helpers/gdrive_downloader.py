import os
import requests
import re

def download_gdrive(url):
    try:
        import yt_dlp
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("Google Drive Error:", e)
        return None
