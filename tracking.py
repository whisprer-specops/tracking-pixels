from flask import Flask, Response
import datetime

app = Flask(__name__)

GIF_PIXEL = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'

@app.route('/track/<uid>')
def track(uid): "some-unique-id"
    with open('opens.log', 'a') as f:
        f.write(f"{datetime.datetime.utcnow()} | {uid}\n")
    
    return Response(
        GIF_PIXEL,
        mimetype='image/gif',
        headers={'Cache-Control': 'no-store, no-cache'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5550)
