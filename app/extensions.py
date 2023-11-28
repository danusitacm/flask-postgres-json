from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please Login to access this page"
login_manager.login_message_category = "warning"
