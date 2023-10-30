from flask import Flask, render_template, request, redirect
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
		task_content = request.form['content']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding task'
	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template("index.html", tasks = tasks)

if __name__ == "__main__":
	app.run(debug = True)

