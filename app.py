# neo4j start 와 open
# pycharm의 재생 누르면 실행 가능
from flask import Flask, jsonify, request, Response, render_template
from neo4j import GraphDatabase

app = Flask(__name__)

class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))


    def delete_users(self): # 모든 유저 관련 정보 삭제
        with self.driver.session() as session:
            greeting = session.write_transaction(self.DELETE_USERS_INFORMATION)
            return greeting
    @staticmethod
    def DELETE_USERS_INFORMATION(tx):
        z = tx.run("MATCH (u:user)"
                   "DELETE u")
        return 'delete all user information success'

greeter = connectDBMS('bolt://localhost:7687','neo4j', '0224')

@app.route('/') # 기본페이지
def home():  # put application's code here
    return 'Hello_world!!'

@app.route('/signup') # 회원가입 페이지
def user_signup():
    a = greeter.sign_users()
    return a

@app.route('/login') # 로그인 페이지
def user_login():
    c = greeter.login_users()
    return c
"""
@app.route('/userLogin', methods=['POST'])
def userLogin():
    user = request.get_json()  # json 데이터를 받아옴
    return jsonify(user)  # 받아온 데이터를 다시 전송

@app.route('/login', methods=['POST']) # 로그인 페이지
def login():
    error = None
    valid_login = 0;
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return valid_login(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 아래의 코드는 요청이 GET 이거나, 인증정보가 잘못됐을때 실행된다.
    return

@app.route('/login/<userName>', methods=['POST']) # 로그인 페이지
def user_Hello():
    return 'hello, %s' #%(userName)
"""
# json 형태로 받아오는 함수 예시
"""
@app.route("/camera", methods=['POST'])
def receive_cam():
    global cam_msg
    c_msg = request.get_json()
    cam_msg = c_msg['flags']  #cam on : 0 | cam off : 1
    print(type(cam_msg), cam_msg)
    return 'received'
    
@app.route("/process", methods=['GET', 'POST'])
def process():
    content = request.json
    result = {'result': True}
    return jsonify(result)
    
"""

@app.route('/user/delete') # 모든 유저들 삭제
def user_delete():
    z = greeter.delete_users()
    return z

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)

# request
# response