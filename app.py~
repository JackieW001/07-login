from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    print request.args
    return render_template("root.html")


@app.route('/response', methods=["GET", "POST"])
def response():
    print request.args
    print request.method
    return render_template("response.html", method=request.method, name=request.args["name"])


if __name__ == '__main__':
	app.debug = True
	app.run()
