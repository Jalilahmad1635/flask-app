from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'change-this-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(240), nullable=False)
    ts = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Note {self.id} {self.author}>"

@app.route('/', methods=['GET', 'POST'])
def board():
    if request.method == 'POST':
        author = request.form['author']
        text = request.form['text']
        db.session.add(Note(author=author, text=text))
        db.session.commit()
        return redirect(url_for('board'))
    items = Note.query.order_by(Note.ts.desc()).all()
    return render_template('index.html', items=items)

@app.route('/add')
def add():
    return redirect(url_for('board'))

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
