import base64
import json
import yaml

from flask import Flask
from flask import request
from flask import jsonify

# import from the 21 Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
from two1 import mkt

# set up server side wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


@app.route('/ocr2speech21')
@payment.required(15000)
def ocr2speech21():
    """
    Detect text in an image using OCR, translate it to English, and generate
    a computer-generated audio clip of it being read.
    """
    try:
        image_url = request.args.get('image_url')
    except:
        return jsonify({'error': 'Missing input arguments.'}, 400)

    try:
        detected_text = mkt.ocr2txt21.detect(image_url=image_url)['text']
    except KeyError:
        return jsonify({'error': 'No text found in image.'}, 400)
    except Exception:
        return jsonify(
            {'error': 'There was an error processing this image.'}, 500)

    try:
        english_text = mkt.translate21.translate(text=detected_text)['results']
    except Exception:
        return jsonify(
            {'error': 'There was an error processing the text.'}, 500)

    try:
        wavfile = mkt.txt2speech21.en({'text': english_text.strip()})
    except Exception:
        return jsonify(
            {'error': 'There was an error processing the text.'}, 500)

    return jsonify(wavfile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6005)
