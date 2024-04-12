import os

from flask import Flask

from views.candidate import candidate_view
from views.voters import voters_view

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__), 
    'uploads'
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(candidate_view)
app.register_blueprint(voters_view)