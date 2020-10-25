# from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     data_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return "<Task {}>".format(self.id)
# @app.route('/')
# def index():
#     #return "Hello, World!"
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True)

# Importing the necessary Libraries
from flask_cors import cross_origin
from flask import Flask, render_template, request
from tts import text_to_speech

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('tts_example.html')
    else:
        return render_template('tts_example.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)