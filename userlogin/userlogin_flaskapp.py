from userlogin_sqlite import *

from flask import Flask, render_template, redirect, request, url_for, request, session, send_file
from functools import wraps
import sqlite3
import os

app = Flask(__name__,static_url_path='/static')
app.secret_key = "cheshirecheese"


def login_required(f):
   @wraps(f)
   def wrap(*args, **kwargs):
      if 'logged_in' in session:
         return f(*args, **kwargs)
      else:
         return redirect(url_for('login'))
   return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():

   mymessage = "Please login..."
   
   if request.method == 'POST':		
      myname = request.form['username']
      mypassword = request.form['password']

      #this uses code from userlogin_sqlite
      results = userlogin(myname, mypassword)

      if results[0] == "Error":
         if results[1] == "Username not found":
             mymessage = "Error: Username not found"
         else:
             mymessage = "Error: Password incorrect"
      else:
         session['logged_in'] = True
         session['username'] = myname
         mymessage = "Welcome " + myname
         return render_template('home.html', message=mymessage)

   return render_template('login.html',message=mymessage)


@app.route('/logout')
@login_required
def logout():
   
   session.pop('logged_in', None)
   session.pop('username', None)
   return redirect(url_for('login'))


@app.route('/')
@app.route('/home')
@login_required
def home():
   
   return render_template('home.html')

@app.route('/webshowusers', methods=['GET','POST'])
@login_required
def webshowusers():

   results = showmeall()
   return render_template('webshowusers.html',rows=results)


@app.route('/webadduser', methods=['GET', 'POST'])
@login_required
def webadduser():

   mymessage = "Enter username and password to add"

   if request.method == 'POST':
      myname = request.form['username']
      mypassword1 = request.form['password1']
      mypassword2 = request.form['password2']

      # this uses code from userlogin_sqlite
      results = adduser(myname, mypassword1,mypassword2,)

      if results[0] == "Error":
         mymessage = results[0] +results[1]
      else:
         mymessage = results[0] +results[1]
         return render_template('home.html', message=mymessage)
   return render_template('webadduser.html',message=mymessage)
   

@app.route('/webupdateuser', methods=['GET', 'POST'])
@login_required
def webupdateuser():

   mymessage = "Enter username and password to update"

   if request.method == 'POST':
      myname = request.form['username']
      mypassword1 = request.form['password1']
      mypassword2 = request.form['password2']

      # this uses code from userlogin_sqlite
      results = adminupdateuser(myname, mypassword1, mypassword2, )

      if results[0] == "Error":
         mymessage = results[0] + results[1]
      else:
         mymessage = results[0] + results[1]
         return render_template('home.html', message=mymessage)
   return render_template('webupdateuser.html',message=mymessage)
   
@app.route('/webdeleteuser', methods=['GET', 'POST'])
@login_required
def webdeleteuser():

   mymessage = "Enter username to delete"

   if request.method == 'POST':
      myname = request.form['username']

      # this uses code from userlogin_sqlite
      results = deleteuser(myname, )

      if results[0] == "Error":
         mymessage = results[0] + results[1]
      else:
         mymessage = results[0] + results[1]
         return render_template('home.html', message=mymessage)

   return render_template('webdeleteuser.html',message=mymessage)


if __name__ == '__main__':
   app.run(debug=True)



