from flask import Flask, render_template
from flask_sqlalchemy import SQLAlcehmy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/products')
def products():
    return 'this is product page'

if __name__== "__main__":
    app.run(debug=True, port=5000)