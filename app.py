from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello nihao"

# this is a test


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
