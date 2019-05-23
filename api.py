from flask import Flask, jsonify, abort, make_response
app = Flask(__name__)

videos = [
    {
        'id': 1,
        'title': 'Roméo Elvis - Viseur ( Audio )',
        'link': 'https://www.youtube.com/watch?v=Y6ZsJYik2lI',
        'duration':'2.47'
    },
    {
        'id': 2,
        'title': 'OrelSan - Dis moi [CLIP OFFICIEL]',
        'link': 'https://www.youtube.com/watch?v=haPpLN2i-Wg',
        'duration':'3.54'
    }
]

@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify({'videos': videos})

@app.route('/video/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = [video for video in videos if video['id'] == video_id]
    if len(video) == 0:
        abort(404)
    return jsonify({'videos': video[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)