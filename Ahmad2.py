
print("| Welcome To Download App |\n") 
import os
import yt_dlp
def download_video():
    url = input("Enter the URL of the video : ").strip()
    quality = input("[4k] or [fhd] or [hd] or [480p] or [360p] or [240p]: ").strip().lower()

    quality_map = {
        "4k": "2160",
        "fhd": "1080",
        "hd": "720",
        "480p": "480",
        "360p": "360",
        "240p": "240"
    }

    height = quality_map.get(quality, "720")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    ydl_opts = {
        # تحميل الفيديو المطلوب فقط بدون بقية قائمة التشغيل
        'noplaylist': True,
        'format': f'bestvideo[height<={height}]+bestaudio/best[height<={height}]/best',
        'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
    }

    print("\n[+] Downloading to Desktop... Please wait ⏳")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[✔] Download Complete Successfully! Check your Desktop 🎉")
    except Exception as e:
        print(f"\n[✘] An error occurred: {e}")

if __name__ == "__main__":
    download_video()