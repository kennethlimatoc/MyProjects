import re
from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from user import User
from plant_info import Plant

app = Flask(__name__)
app.secret_key = 'keep_it_secret'
bcrypt = Bcrypt(app)


def validate_password(password):
    if len(password) < 8 or len(password) > 32:
        return False, "Password must be 8-32 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least 1 uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least 1 lowercase letter"
    return True, ""


@app.route('/')
def login_page():
    return redirect('/login')

@app.route('/login')
def show_login():
    return render_template('user_login.html')

@app.route('/login', methods=['POST'])
def login_user():
    user = User.get_by_username(request.form['username'])
    if not user or not bcrypt.check_password_hash(user.password_hash, request.form['password']):
        flash("Incorrect Password or Incorrect Username.", "login_error")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/home')

@app.route('/register')
def show_register():
    return render_template('user_registration.html')

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    if len(username) != 8:
        flash("Username must be exactly 8 characters long", "register_error")
        return redirect('/register')

    is_valid, message = validate_password(password)
    if not is_valid:
        flash(message, "register_error")
        return redirect('/register')

    if password != request.form['confirm_password']:
        flash("Passwords do not match", "register_error")
        return redirect('/register')

    hashed_pw = bcrypt.generate_password_hash(password)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "username": username,
        "password_hash": hashed_pw
    }
    User.save(data)
    flash("Account registered successfully. Please log in.", "register_success")
    return redirect('/login')


@app.route('/profile')
def view_profile():
    if 'user_id' not in session:
        return redirect('/login')
    user = User.get_by_id({'id': session['user_id']})
    return render_template('my_profile.html', user=user)


@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect('/login')

    new_password = request.form.get('new_password')

    if new_password:
       
        if len(new_password) < 8:
            flash("Password must be at least 8 characters long.", "profile_error")
            return redirect('/profile')

        is_valid, message = validate_password(new_password)
        if not is_valid:
            flash(message, "profile_error")
            return redirect('/profile')

        if new_password != request.form['confirm_password']:
            flash("New passwords do not match", "profile_error")
            return redirect('/profile')

        hashed_pw = bcrypt.generate_password_hash(new_password)
    else:
        user = User.get_by_id({'id': session['user_id']})
        hashed_pw = user.password_hash

    data = {
        "id": session['user_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "username": request.form['username'],
        "password_hash": hashed_pw
    }

    User.update(data)
    flash("Profile updated successfully!", "profile_success")
    return redirect('/profile')



@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/login')

    user = User.get_by_id({'id': session['user_id']})
    plants = Plant.get_all_by_user({'user_id': session['user_id']})
    return render_template('home.html', user=user, plants=plants)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/add')
def show_add_plant():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('add_plant.html')

@app.route('/add', methods=['POST'])
def save_plant():
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        "plant_name": request.form['plant_name'],
        "plant_type": request.form['plant_type'],
        "tools_and_materials": request.form['tools_and_materials'],
        "plants_component": request.form['plants_component'],
        "procedure": request.form['procedure'],
        "user_id": session['user_id']
    }
    Plant.save(data)
    return redirect('/home')

@app.route('/view/<int:id>')
def view_plant(id):
    if 'user_id' not in session:
        return redirect('/login')
    plant = Plant.get_by_id({'id': id})
    return render_template('view_plant.html', plant=plant)


@app.route('/edit/<int:id>')
def edit_plant(id):
    if 'user_id' not in session:
        return redirect('/login')
    plant = Plant.get_by_id({'id': id})
    return render_template('update.html', plant=plant)

@app.route('/update/<int:id>', methods=['POST'])
def update_plant(id):
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        "id": id,
        "plant_name": request.form['plant_name'],
        "plant_type": request.form['plant_type'],
        "tools_and_materials": request.form['tools_and_materials'],
        "plants_component": request.form['plants_component'],
        "procedure": request.form['procedure']
    }
    Plant.update(data)
    return redirect('/home')


@app.route('/delete/<int:id>')
def delete_plant(id):
    if 'user_id' not in session:
        return redirect('/login')
    Plant.delete({'id': id})
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True)
