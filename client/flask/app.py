from flask import Flask, request, send_file, Response

from flask import jsonify
import io
from flask_cors import CORS
from modules.replikate import Replikate
from environment import PORT_FLASK, REPLIKATE_VIDEO_MANAGER_ALIASES

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
replikate: Replikate = None
@app.route('/upload',  methods=['POST'])
def upload():
    global replikate
    if not replikate:
        replikate = Replikate(REPLIKATE_VIDEO_MANAGER_ALIASES)
    title = request.form['title']
    description = request.form['description']
    file = request.files['file']
    blob = file.read()
    video = {
        "title": title,
        "description": description,
        "blob": blob,
        "size": len(blob)
    }

    video = replikate.store_video(video)
    response = jsonify(video)
    return response

@app.route('/stream')
def stream():
    global replikate
    if not replikate:
        replikate = Replikate(REPLIKATE_VIDEO_MANAGER_ALIASES)
    video_id = request.args.get('id')
    print(video_id)
    blob = replikate.stream_video(video_id)
    blob = io.BytesIO(blob)
    return send_file(blob, mimetype='video/mp4')

@app.route('/videos', methods=['GET'])
def list():
    global replikate
    if not replikate:
        replikate = Replikate(REPLIKATE_VIDEO_MANAGER_ALIASES)
    videos = replikate.index_videos()
    response = jsonify(videos)
    return response

@app.route('/video', methods=['GET'])
def get():
    global replikate
    if not replikate:
        replikate = Replikate(REPLIKATE_VIDEO_MANAGER_ALIASES)
    video_id = request.args.get('id')
    video: dict = replikate.read_video(video_id)
    response = jsonify(video)
    return response

@app.route('/video', methods=['DELETE'])
def delete():
    global replikate
    if not replikate:
        replikate = Replikate(REPLIKATE_VIDEO_MANAGER_ALIASES)
    video_id = request.args.get('id')
    video = replikate.delete_video(video_id)
    response = jsonify(video)
    return response

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']='*'
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    app.run(debug=True, port=PORT_FLASK)
