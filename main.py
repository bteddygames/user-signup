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
    is_good=False

    passone_error=''
    passtwo_error=''
    user_error=''
    email_error=''

    for char in username:
        if char==' ':
            user_error='Not a valid username'
            username=''
    
    if len(username)<3 or len(username)>20:
        user_error='Not a valid username'
        username=''
    
    if passone==' ' or len(passone)<3 or len(passone)>20:
        passone_error='Not a valid password'
        passone=''
    
    if passtwo==' ' or len(passtwo)<3 or len(passtwo)>20:
        passtwo_error='Not a valid password'
        passtwo=''

    if passone!=passtwo:
        passone_error="Invalid Password Combination"
        passtwo_error="Invalid Password Combination"
        passone=''
        passtwo=''

    for char in email:
        if char==check:
            is_good=True
    
    if is_good==False:
        email_error="Invalid email"  
        email=''     
    
    for chart in email:
        if chart=='.':
            count+=1
    
    if count!=1:
        email_error="To few or to many periods"
        email=''

    if email:
        if not user_error and not passone_error and not passtwo_error and not email_error:
            return redirect('/welcome?username={0}'.format(username))

    if not user_error and not passone_error and not passtwo_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('base.html', passone_error=passone_error, 
            passtwo_error=passtwo_error, user_error=user_error, 
            username=username, passone=passone, passtwo=passtwo,
            email_error=email_error, email=email)

@app.route('/welcome')
def welcome():
    username= request.args.get('username')
    return render_template('welcome.html', username=username)

app.run() 
