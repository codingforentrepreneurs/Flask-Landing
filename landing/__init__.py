import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
csrf = CSRFProtect(app)

# don't share in production
# secret key 
# wtf csrf secret key

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
    SECRET_KEY="4b332#@@1!74-006b-4889-8#@#-67b#@#b90ddffd",
    WTF_CSRF_SECRET_KEY='8207bece0139#4980!af20a681e3bf56f3',
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
))

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .views import *
from .home.views import *
from .jobs.views import *
from .profiles.views import *
