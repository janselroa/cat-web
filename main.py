from flask import Flask
from flask import request,render_template,flash,url_for,redirect
from flask_mail import Mail,Message
import os
import functions

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

@app.route('/random_cat')
def cat_random():
	gatos = functions.generar_cat()
	return render_template("cat_random.html",gatos=gatos)

@app.route('/races_cat')
def races_cat():
	return render_template("races_cat.html")

@app.route('/contacto',methods=['GET','POST'])
def contacto():
	if request.method == 'GET':
		return render_template('contacto.html')

	elif request.method == 'POST':
		mensaje = [request.form['asunto'],request.form['name'],request.form['mensaje']]
		mensajes = list(map(functions.limpiar_str,mensaje))
		msg = Message(recipients=[os.environ['EMAIL']],
			body=mensaje[2],
			subject=mensaje[0]
		)
		mail.send(msg)
		flash('Gracias email enviado correctamente')
		return redirect(url_for('contacto'))
	else:
		return "Error"


app.run()
