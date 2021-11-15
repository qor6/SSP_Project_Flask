# neo4j start 와 open
# pycharm의 재생 누르면 실행 가능
from flask import Flask
from neo4j import GraphDatabase
# import json

app = Flask(__name__)

class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def create_users(self): # 회원가입 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.INSERT_USERS_INFORMATION)
            return greeting

    def delete_users(self): #
        with self.driver.session() as session:
            greeting = session.write_transaction(self.DELETE_USERS_INFORMATION)
            return greeting

    @staticmethod # (u:user:username)
    def INSERT_USERS_INFORMATION(tx):
        a = tx.run("CREATE (u:user{name : $username, id : $user_id, password : $user_password, nickname:$nickname})",
                   username = "", user_id ="", user_password = "", nickname = "")
        return 'add user information success'

    @staticmethod
    def DELETE_USERS_INFORMATION(tx):
        z = tx.run("MATCH (u:user)"
                   "DELETE u")
        return 'delete all user information success'

greeter = connectDBMS('bolt://localhost:7687','neo4j', '0224')

@app.route('/') # 기본페이지
def home():  # put application's code here
    return 'Hello!!'

@app.route('/create') # 회원가입 페이지
def user_add():
    a = greeter.create_users()
    return a

@app.route('/user/delete') # 모든 유저들 삭제
def user_delete():
    z = greeter.delete_users()
    return z

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)

# request
# response