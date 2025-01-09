from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    options = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
