from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    a = range(100000)
    print a
    return "OK"


app.config.update(
    DEBUG=True
)

if __name__ == '__main__':
    app.run(port=5000)
