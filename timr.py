from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "The time is %s" % datetime.now().strftime("%d.%m.%Y %H:%M")

if __name__ == "__main__":
    app.run()
