from app import app
import os

app.config['SECRET_KEY'] = os.urandom(32)


