from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '7by3489cx2v5b6vc3478n5t678r3dhng67wengrdq9283nbcvf968bnrvc43wn7v5b34t6789n5367890v5nbw9ncv5t37689vc534gv6346bvw456'
food_options = ['soup', 'fish', 'cat']



@app.route('/')
def home():
    if 'usertype' in session:
        mode = session.get('usertype')
        name = session.get('name')
        return redirect(f'/endpoint?username={name}&mode={mode}')
    else:
        return render_template('index.html')

@app.route('/endpoint')
def endpoint():
    mode = request.args['mode']
    username = request.args['username']
    
    if mode == 'chooser':
        session['usertype'] = 'chooser'
        session['name'] = username
        if len(food_options) == 0:
            return render_template('error.html', error='Food options were not chosen yet.')
        else:
            return render_template("choose.html", options=food_options, name=username)
    elif mode == 'cooker':
        session['usertype'] = 'cooker'
        session['name'] = username
        if len('food_options') == 0:
            return render_template('set_choises.html')
        else:
            return render_template('results.html')

@app.route('/submit-response/<option>/<name>')
def submit(option, name):
    return "submit route"

@app.route("/clear-choise")
def clear():
    session.clear()
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)