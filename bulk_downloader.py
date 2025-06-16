import yt_dlp

def download_mp3s_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'music/%(title)s.%(ext)s',
        'noplaylist': True,
        'ffmpeg_location': r"D:\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"  # <-- Add this line
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == '__main__':
    download_mp3s_from_file('links.txt')
