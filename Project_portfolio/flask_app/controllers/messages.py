# from crypt import methods
from email import message_from_binary_file
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
# from flask_app.controllers.users import message


@app.route('/message/create', methods=['POST'])
def createMessage():
    # if not Message.validate_message(request.form):
    #     return redirect('/message')
    data ={ 
        "user_id": request.form['user_id'],
        "messages": request.form['message']
    }
    if not Message.validate_message(data):
        return redirect('/message')
    Message.save(data)
    return redirect('/message') 

@app.route('/message/edit/<int:messages>')
def update(messages):
    if 'user_id' not in session:
        return redirect('/login')
    data ={
        'id': session['user_id']
    }
    data2 ={
        'user_id': session['user_id']
    }
    return render_template("edit.html", messages=Message.getMessagesByUserId(data2), user=User.get_by_id(data))


@app.route('/message/update/<int:messages>',methods=['POST'])
def update_message(messages):
    data ={
        'id' : messages,
        "user_id": request.form['user_id'],
        "messages": request.form['message']
    }
    Message.update(data)
    return redirect('/message')




# @app.route('/message/create', methods=['POST'])
# def createMessage():
#     # if not Message.validate_message(request.form):
#     #     return redirect('/message')
#     data ={ 
#         "user_id": request.form['user_id'],
#         "messages": request.form['message']
#     }
#     if not Message.validate_message(data):
#         return redirect('/message')
#     Message.save(data)
#     return redirect('/message') 







@app.route('/message')
def message():
    if 'user_id' not in session:
        return redirect('/login')
    data ={
        'id': session['user_id']
    }
    data2 ={
        'user_id': session['user_id']
    }
    return render_template("messages.html", messages=Message.getMessagesByUserId(data2), user=User.get_by_id(data))

@app.route('/message/delete/<int:messages>')
def delete(messages):
    data ={
        'id' : messages
    }
    Message.destroy(data)
    return redirect('/message')




@app.route('/examples')
def examples():
    return render_template("examples.html")


# @app.route('/message/update/<int:messages>')
# def update2(messages):
#     data ={
#         'id' : messages
#     }
#     Message.update(data)
#     return redirect('/message/update')

    # @app.route('/register',methods=['POST'])
# def register():

#     if not User.validate_register(request.form):
#         return redirect('/')
#     data ={ 
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email'],
#         "password": bcrypt.generate_password_hash(request.form['password'])
#     }
#     id = User.save(data)
#     session['user_id'] = id