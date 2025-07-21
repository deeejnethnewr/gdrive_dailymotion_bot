def download_dailymotion(url):
    try:
        import yt_dlp
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("Dailymotion Error:", e)
        return None
