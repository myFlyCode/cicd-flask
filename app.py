from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"

# this is a test


if __name__ == "__main__":
    app.run()
