from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def validate_time():

    username= request.form['username']
    passone= request.form['passone']
    passtwo= request.form['passtwo']
    email= request.form['email']

    check="@"
    dot='.'
    count=0

    passone_error=''
    passtwo_error=''
    user_error=''
    check_error=''

    if username==' ' or len(username)<3 or len(username):
        user_error='Not a valid username'
        username=''
    
    if passone==' ' or len(passone)<3 or len(passone)>20:
        passone_error='Not a valid password'
        passone=' '
    
    if passtwo=='' or len(passtwo)<3 or len(passtwo)>20:
        passtwo_error='Not a valid password'
        passtwo=''

    if passone!=passtwo:
        passone_error="Invalid Password Combination"
        passtwo_error="Invalid Password Combination"
        passone=''
        passtwo=''

    for char in email:
        if check:
            continue
        else:
            check_error="That is not a valid email"
        for chart in email:
            if dot:
                count=1
        if count<1 and count>1:
            check_error="To few or to many periods"
        else:
            continue

    if not user_error and not passone_error and not passtwo_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('base.html', passone_error=passone_error, 
            passtwo_error=passtwo_error, user_error=user_error, 
            username=username, passone=passone, passtwo=passtwo,
            check_error=check_error, email=email)

@app.route('/welcome')
def welcome():
    username= request.args.get('username')
    return render_template('welcome.html', username=username)

app.run() 
