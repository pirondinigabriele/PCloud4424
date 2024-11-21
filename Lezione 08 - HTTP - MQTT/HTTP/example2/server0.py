from flask import Flask,request
import json

#web server con Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    return 'ciao'

@app.route('/ciao',methods=['GET'])
def main2():
    return 'ciao, ciao'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)




