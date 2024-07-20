from flask import Flask

#a flask application instance
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'my_secrt_key'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+mysqldb://localhost'

if __name__ == '__main':
    app.run(debug=True)