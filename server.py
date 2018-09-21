from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/results')
def show_results():
    mood = request.args.get("name")

    if mood == "cheery":
        message = "It's a wonderful day!"
    elif mood == "honest":
        message = "I hope you get more sleep tonight"
    elif mood == "dreary":
        message = "I'll put the coffee pot on"
    return render_template('results.html', message=message)

@app.route('/save-name')
def savename():
    name = request.args.get("name")

    session['name'] = name
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
