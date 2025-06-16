from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to this backend

@app.route('/download', methods=['POST'])
def download_mp3s():
    data = request.get_json()
    urls = data.get('urls', [])
    if not urls:
        return jsonify({'error': 'No URLs provided'}), 400

    # Ensure music folder exists
    os.makedirs("music", exist_ok=True)

    # yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'demo/%(title)s.%(ext)s',
        'noplaylist': True,
        'ffmpeg_location': r"D:\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        return jsonify({'message': 'MP3s downloaded in /music'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
