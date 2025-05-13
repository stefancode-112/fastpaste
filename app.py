from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = 'simulasi-aman'

CREDENTIALS = {
    'stefan.d.spaulding@gmail.com': '' #Dont Forget to clear the password
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in CREDENTIALS and CREDENTIALS[email] == password:
            session['email'] = email
            return redirect('/dashboard')
        return render_template('login.html', error='Login gagal.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect('/')
    return render_template('dashboard.html', email=session['email'])

if __name__ == '__main__':
    app.run(debug=True)
