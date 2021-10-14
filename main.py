from flask import Flask
from flask import request,render_template,flash,url_for,redirect
from flask_mail import Mail,Message
import os

app = Flask(__name__)

app.config['SECRET_KEY']=os.environ['secret_key']
#configurando Flask Email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['EMAIL']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['EMAIL']

mail = Mail(app)


@app.route("/")
def index():
	imagenes = os.listdir("static/img/gatos")
	return render_template("index.html",imagenes=imagenes)

@app.route('/random-cat')
def cat_random():
	return render_template("cat_random.html")

@app.route('/races-cat')
def races_cat():
	return render_template("races_cat.html")

@app.errorhandler(404)
def error404(e):
	return render_template("404.html"),404


@app.route('/about',methods=['GET','POST'])
def about():
	if request.method == 'GET':
		return render_template('contacto.html')

	elif request.method == 'POST':
		mensaje = [request.form['asunto'],request.form['name'],request.form['mensaje']]
		msg = Message(recipients=[os.environ['EMAIL']],
			body=mensaje[2],
			subject=mensaje[0]
		)
		mail.send(msg)
		flash('Gracias email enviado correctamente')
	else:
		return "Error"


app.run(debug=True)
