from flask import Flask
from neo4j import GraphDatabase
import json

app = Flask(__name__)

class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def insert_users(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.INSERT_USERS_INFORMATION)
            return greeting

    def delete_users(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.INSERT_USERS_INFORMATION)
            return greeting

    @staticmethod
    def INSERT_USERS_INFORMATION(tx):
        a = tx.run("CREATE (n:user{name : $username, id : $user_id, password : $user_password, nickname:$nickname})", username = "", user_id ="", user_password = "", nickname = "")
        return 'apple computer is best'

    @staticmethod
    def DELETE_USERS_INFORMATION(tx):
        a = tx.run("MATCH (n:user)""DELETE n")
        return 'apple computer is worst'

greeter = connectDBMS('bolt://localhost:7687','neo4j', '0224')


@app.route('/') # 기본페이지
def home():  # put application's code here
    return 'Hello World!'

@app.route('/Add_User') #
def home_setting():  # put application's code here
    a = greeter.insert_users()
    return a


if __name__ == '__main__':
    app.run(debug=True)
