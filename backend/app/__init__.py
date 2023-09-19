from flask import Flask
from app.routes.health import health_bp
from app.routes.users import users_bp
from app.routes.error import error_bp
from app.routes.auth import auth_pb
from app.routes.group import groups_bp
from app.database import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_pb)
    app.register_blueprint(groups_bp)
    app.register_blueprint(error_bp)
    return app
