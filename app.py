from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)

appleComputer = ['iphone', 'ipad', 'ipod', 'mac']
class connectDBMS :
    def __init__(self, url, user, password) :
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def insert_apple(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.INSERT_APPLEDATA)
            return greeting

    def delete_apple(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self.DELETE_APPLEDATA)
            return greeting

@staticmethod
def INSERT_APPLEDATA(tx):
    for i in range(0,4):
       a = tx.run("CREATE (n:apple_product{name : $appleComputer})", appleComputer = appleComputer[i])
    return 'apple computer is best'

    @staticmethod
    def DELETE_APPLEDATA(tx):
        a = tx.run("MATCH (n:apple_product)"
                   "DELETE n")
        return 'apple computer is worst'

greeter = connectDBMS('bolt://localhost:7687','neo4j', '1234')


@app.route('/') # 기본페이지
def main():  # put application's code here
    return 'Hello World!'

@app.route('/setting') #
def setting():  # put application's code here
    a = greeter.insert_apple()
    return a

@app.route('/home') #
def home():  # put application's code here
    a = greeter.delete_apple()
    return a

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
