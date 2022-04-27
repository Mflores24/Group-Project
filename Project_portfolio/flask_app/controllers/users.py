from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/interests')
def interests():
    return render_template("interests.html")


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/login')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/message')

@app.route('/login/process',methods=['POST'])
def login_process():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/message')
    session['user_id'] = user.id
    return redirect('/message')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')