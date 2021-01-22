from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def helllo():
    return "hello, flask!"

@app.route("/coffee", methods=['POST'])
def coffee():
    req = request.get_json()

    url = req["action"]["detailParams"]["words"]["value"]    # read json file
                # req["action"]["detailParams"][파리미터 명]["value"]

    url = "https://github.com/meotitda/DICTIONARY/blob/master/DIC/A/AST.md"
    # answer = 

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "title",
                        "description": "description",
                        "thumbnail": {
                            "imageUrl": url
                        },
                    },
                    "profile": {
                        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                        "nickname": "보물상자"
                    },
                    "social": {
                        "like": 1238,
                        "comment": 8,
                        "share": 780
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)