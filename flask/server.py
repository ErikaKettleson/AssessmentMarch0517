from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# YOUR ROUTES GO HERE


@app.route('/')
def show_homepage():
    """show homepage template"""
    return render_template("index.html")


@app.route('/application-form.html')
def apply():
    """show the application page"""
    return render_template("application-form.html")


@app.route('/application-success.html', methods=['POST', 'GET'])
def success():
    """show the response/success page"""
    if request.method == 'POST':
        # import ipdb; ipdb.set_trace()
        name = request.form["firstname"]
        last = request.form["lastname"]
        money = request.form["salary"]
        position = request.form["jobtype"]
        return render_template("application-success.html",
                               first=name,
                               surname=last,
                               salary=float(money),
                               job=position,
                               )
        # else:
        #     return render_template('application-form.html')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="localhost")
