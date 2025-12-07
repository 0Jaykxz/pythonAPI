from routes.home import home_route
from routes.users import user_route
from database.database import db
from database.models.user import lojas

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(user_route, url_prefix="/@")

def configure_db():
    db.connect()
    db.create_tables([lojas])