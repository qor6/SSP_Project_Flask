# neo4j start 와 open
# pycharm의 재생 누르면 실행 가능
from flask import Flask, jsonify, request, Response, render_template
from neo4j import GraphDatabase

app = Flask(__name__)

class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def sign_users(self): # 회원가입 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.SIGNUP_USERS_INFORMATION)
            return greeting


    def login_users(self): # 로그인 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.LOGIN_USERS_INFORMATION)
            return greeting

    def calendar(self, date):  # 캘린더 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.CALENDAR,date)
            return greeting

    def todolist(self):  # To do 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.TODOLIST)
            return greeting

    def todolist_con(self):  # To do 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.TODOLIST_CON)
            return greeting

    def d_day_users(self): # D-day 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.D_DAY_USERS)
            return greeting

    def motto_users(self): # 좌우명 관련
        with self.driver.session() as session:
            greeting = session.write_transaction(self.MOTTO_USERS)
            return greeting

    @staticmethod  # (u:user:username)
    def SIGNUP_USERS_INFORMATION(tx):
        a = tx.run("CREATE (n:user{name : $username, id : $user_id, pw : $user_password, nickname:$nickname})",
               username="", user_id="", user_password="", nickname="")
        return 'singup: add user information success'

    @staticmethod
    def LOGIN_USERS_INFORMATION(tx):
        b = tx.run("MATCH (n:user)"
                   "RETURN n")
        return 'login success'

    @staticmethod
    def CALENDAR(tx, date):
        year = date[0:2]
        month = date[2:4]
        day = date[4:6]
        c = tx.run("CREATE (d:date {year = $year, month = $month, day = $day})",
                   year="", month="", day="")
        return 'create calendar date'

    @staticmethod
    def TODOLIST(tx):
        d = tx.run("CREATE (l:list {text: $text, date: $ date})",
                   text="", date="")
        return 'create todolist'

    @staticmethod
    def TODOLIST_CON(tx):
        e = tx.run("MATCH (list:list, date:date)"
                   "WHERE list.date = date"
                   "CREATE (list:list) -[:include] -> (data:date)"                                   
                   "RETURN list, date")
        return 'connect todolist and date'

    @staticmethod  # (u:user:username)
    def D_DAY_USERS(tx):
        f = tx.run("CREATE (d:d_day")
        return 'd_day success'

    @staticmethod  # (u:user:username)
    def MOTTO_USERS(tx):
        g = tx.run("CREATE (m:motto{contents : $contents})",
               motto="")
        return 'create motto'

    def delete_users(self): # 모든 유저 관련 정보 삭제
        with self.driver.session() as session:
            greeting = session.write_transaction(self.DELETE_USERS_INFORMATION)
            return greeting

    @staticmethod
    def DELETE_USERS_INFORMATION(tx):
        z = tx.run("MATCH (n:user)"
                   "DELETE n")
        return 'delete all user information success'

greeter = connectDBMS('bolt://localhost:7687','neo4j','0224')

@app.route('/') # 기본페이지
def home():  # put application's code here
    return 'Hello_world!!'

@app.route('/signup') # 회원가입 페이지
def user_signup():
    a = greeter.sign_users()
    return a

@app.route('/login') # 로그인 페이지
def user_login():
    b = greeter.login_users()
    return b

@app.route('/calender') #  캘린더 페이지
def calendar():
    date = request.get_json()  # json 데이터를 받아옴
    c = greeter.calendar(date)
    return  c

@app.route('/todolist') # todolist 페이지
def todolist():
    d = greeter.todolist()
    return d

@app.route('/todolist_con') # todolist 연결 페이지
def todolistcon():
    e = greeter.todolist_con()
    return e

@app.route('/d_day_users') # d-day 연결 페이지
def d_day_users():
    f = greeter.d_day_users()
    return f

@app.route('/motto_users') # motto 연결 페이지
def motto_users():
    g = greeter.motto_users()
    return g

"""
@app.route('/userLogin', methods=['POST'])
def userLogin():
    user = request.get_json()  # json 데이터를 받아옴
    return jsonify(user)  # 받아온 데이터를 다시 전송

@app.route('/login', methods=['POST']) # 로그인 페이지
def login():
    error = None
    login = 0;
    if request.method == 'POST':
        if login(request.form['username'],
                       request.form['password']):
            return login(request.form['username'])
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