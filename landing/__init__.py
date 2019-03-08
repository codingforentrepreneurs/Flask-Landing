from flask import Flask

app = Flask(__name__)

from .views import *
from .home.views import *
from .jobs.views import *
from .profiles.views import *
