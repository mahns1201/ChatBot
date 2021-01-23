from flask import Flask, request, jsonify

app = Flask(__name__)

def make_url(input_text):
    url = "https://github.com/meotitda/DICTIONARY/blob/master/DIC/"
    
    input_text = input_text.upper()
    detail = input_text[0] + '/' + input_text + '.md'

    url = url + detail

    return url

@app.route("/words", methods=['POST'])
def movies():
    req = request.get_json()
    
    input_text = req['userRequest']['utterance'] # 사용자가 전송한 실제 메시지
    
    url = make_url(input_text)

    # 카드 리스트형 응답용 메시지
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": url
                    }
                }
            ]
        }
    }            

    return jsonify(res)