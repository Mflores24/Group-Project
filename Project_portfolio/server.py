from flask_app import app

from flask_app.controllers import users,messages,surveys,like_unlike

if __name__=="__main__":
    app.run(debug=True)