import math
from flask import Flask, request, Response
app = Flask(__name__)
def parse(number):
    if number is None:
        return None
    if not (number.isascii() and number.isdigit()):
        return None
    return int(number)
@app.route("/1a_aarturr_r1_gmail_com")
def lcm_handler():
    x = parse(request.args.get("x"))
    y = parse(request.args.get("y"))
    if x is None or y is None:
        text = "NaN"
    else:
        text = str(math.lcm(x, y))
    return Response(text, mimetype="text/plain")
if __name__ == "__main__":
    app.run()
