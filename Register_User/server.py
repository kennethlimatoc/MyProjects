from flask import Flask, render_template, request

app = Flask(__name__)

# Home route (form page)
@app.route('/')
def index():
    return render_template("registered.html")   # <-- your form HTML goes here

# Handle form submission
@app.route('/display_text', methods=['POST'])
def display_user():
    name = request.form['txt-name']
    age = request.form['txt-age']
    return render_template('display.html', user_name=name, user_age=age)

if __name__ == '__main__':
    app.run(debug=True)
