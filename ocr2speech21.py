import base64
import two1.mkt as mkt

image_url = 'http://i.imgur.com/U86mtM1.png'

chinese_text = mkt.ocr2txt21.detect(image_url=image_url)['text']

english_text = mkt.translate21.translate(text=chinese_text)['results']

wavfile = mkt.txt2speech21.en({'text': english_text.strip()})['data']
with open('output.wav', 'wb') as file:
    file.write(base64.b64decode(wavfile))
    file.close()
