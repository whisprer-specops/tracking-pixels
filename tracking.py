from flask import Flask, Response
import datetime

app = Flask(__name__)

GIF_PIXEL = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'

@app.route('/track/<uid>')
def track(uid):
    # log whatever you want here
    "Well i'll be damned - it actually works - look here's the proof, an actual message triggered by a tracking pixel!"
    print(f"{datetime.datetime.utcnow()} | opened by {uid}")
    
    return Response(
        GIF_PIXEL,
        mimetype='image/gif',
        headers={'Cache-Control': 'no-store, no-cache'}
    )