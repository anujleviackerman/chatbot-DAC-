from flask import Flask, render_template, url_for,request
import socket
import time
import pickle
HEADERSIZE = 10




app = Flask(__name__)

@app.route('/')

def index():
    return render_template('register.html')

#register
@app.route('/register', methods=['POST'])
def register():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))

    uname=request.form['username']
    ps=request.form['password']
    em=request.form['email']
    dict = {"code_from":"reg","username":uname,"password":ps,"email":em}
    msg = pickle.dumps(dict)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    s.send(msg)
    return render_template('login.html',checkbool=True)

#login
@app.route('/login', methods=['POST'])
def login():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))

    ps=request.form['password']
    em=request.form['email']
    dict = {"code_from":"login","password":ps,"email":em}
    msg = pickle.dumps(dict)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    s.send(msg)
    oi=s.recv(1024)
    if oi==b'True':
        return render_template('ai.html')
        
    elif oi==b'False':
        return render_template('login.html')
        
    
#aiweb
@app.route('/ai', methods=['POST'])
def ai():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1242))
    ui=request.form['userinput']
   
    print(ui)
    s.send(ui.encode('utf-8'))
    oi=s.recv(1024)
    print("oi:")
    print(oi)
    return render_template('ai.html',ui=ui,oi=oi)



if __name__=="__main__":
    app.run(debug=True)