from flask import Flask
from config import app_config, mongo_config
from Controllers import PageRoutes, ErrorRoutes
import os


app = Flask(__name__)

# app settings
app.secret_key = '1'
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'


# blueprints init
blueprints = [
    PageRoutes.mod
]
for bp in blueprints:
    app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host="localhost", port=5010, debug=True)
