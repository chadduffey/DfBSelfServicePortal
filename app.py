from flask import Flask, render_template, redirect, url_for, g

import forms
import urllib2

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'ooogaboogaoooga'

#tuesday
#modify static form to be a form model
#route for options...
#route for completion


@app.route('/', methods=('GET', 'POST'))
def index():
	form = forms.LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('register'))
	return render_template('main.html', form=form)

@app.route('/register', methods=('GET', 'POST'))
def register():
	form = forms.Register()
	if form.validate_on_submit():
		return redirect(url_for('complete'))
	return render_template('register.html', form=form)

@app.route('/complete', methods=('GET', 'POST'))
def complete():
	#build a urllibrequest to the DfB API
	request = urllib2.Request('https://api.dropbox.com/1/team/members/add')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization','Bearer token')
	body = str('{  "member_email": "mike@dbtests.info", "member_given_name": "Mike", "member_surname": "McMahon", "send_welcome_email": true}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	return render_template('complete.html')

if __name__ == '__main__':
	app.run(debug=DEBUG, host=HOST, port=PORT)