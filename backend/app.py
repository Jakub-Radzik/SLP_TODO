import datetime
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from API.tasks import tasks
from API.users import users

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'JanuszPawlacz2137'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=2)

app.register_blueprint(users)
app.register_blueprint(tasks)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
