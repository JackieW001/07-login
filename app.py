from flask import Flask, render_template, request, session

test_username = "user"
test_password = "passwrd"

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=["GET"])
def root():
    print request.args
    if session['username'] is not None:
        return render_template("welcome.html", name=session['username'])
    return render_template("root.html", error="")


@app.route('/welcome', methods=["GET", "POST"])
def response():
    if request.args['username'] == test_username and request.args['password'] == test_password:
        session['username'] = request.args['username']
        return render_template("welcome.html", name=request.args["username"])

    elif request.args['username'] != test_username:
        return render_template("root.html", error="Bad username.")

    elif request.args['password'] != test_password:
        return render_template("root.html", error="Bad password.")

    return render_template("root.html", error="You should not get to this point." )

if __name__ == '__main__':
	app.debug = True
	app.run()
