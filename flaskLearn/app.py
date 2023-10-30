from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# database config & init
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	# return task and id every time it is created
	def __repr__(self):
		return '<Task %r>' % self.id

# on the "homepage", do:
@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		return 'hello'
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True)

