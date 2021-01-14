from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def helllo():
    return "hello, flask!"

@app.route("/coffee", methods=['POST'])
def coffee():
    req = request.get_json()

    coffee_menu = req["action"]["detailParams"]["coffee_menu"]["value"]    # read json file
                # req["action"]["detailParams"][파리미터 명]["value"]

    answer = coffee_menu
    # answer = "아메리카노"

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)