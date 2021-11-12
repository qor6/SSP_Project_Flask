# neo4j의 brower에 start 와 open
# 파이참의 재생 누르면 실행 가능
from flask import Flask
from neo4j import GraphDatabase
# import json

app = Flask(__name__)

class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def create_users(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.INSERT_USERS_INFORMATION)
            return greeting

    def delete_users(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.DELETE_USERS_INFORMATION)
            return greeting

    @staticmethod # (n:user:username)
    def INSERT_USERS_INFORMATION(tx):
        a = tx.run("CREATE (n:user{name : $username, id : $user_id, password : $user_password, nickname:$nickname})",
                   username = "", user_id ="", user_password = "", nickname = "")
        return 'add user information success'

    @staticmethod
    def DELETE_USERS_INFORMATION(tx):
        a = tx.run("MATCH (n:user)""DELETE n")
        return 'delete all user information success'

greeter = connectDBMS('bolt://localhost:7687','neo4j', '0224')


@app.route('/') # 기본페이지
def home():  # put application's code here
    return 'Hello!!'

@app.route('/user/add') #주소창에 /user/add로 입력하면
def user_add():  # put application's code here
    a = greeter.create_users()
    return a

@app.route('/user/delete')
def user_delete():  # put application's code here
    a = greeter.delete_users()
    return a

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)