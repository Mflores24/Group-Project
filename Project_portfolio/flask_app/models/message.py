from pyexpat.errors import messages
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    db_name = "portfolio_schema"
    def __init__(self,data):
        self.id = data['id']
        self.messages = data['messages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def getMessagesByUserId(cls,data):
        query = "SELECT * FROM messages WHERE user_id = %(user_id)s "
        print(query)
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def save(cls,data):
        query = "INSERT INTO messages (messages, user_id) VALUES (%(messages)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def getLikesByUserId(cls,data):
        query = " SELECT * FROM messages WHERE user_id = %(user_id)s JOIN likes WHERE message_id = %(message_id)s"

    @classmethod
    def likeMessage(cls,data):
        query = "Insert INTO likes (user_id, message_id) VALUES (%(user_id)s, %(message_id)s);"



    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM instruments WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE messages SET messages=%(messages)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['messages']) <= 4:
            flash(" Message must be at least 5 characters!!!.","message")
            is_valid=False
        return is_valid


