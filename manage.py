from flask import Flask
from config import app_config, mongo_config
from Controllers import Queries, PageRoutes, ErrorRoutes, Indexes
import os


app = Flask(__name__)

# app settings
app.secret_key = '1'
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'


# blueprints init
blueprints = [
    PageRoutes.mod,
    Queries.mod,
    Indexes.mod
]
for bp in blueprints:
    app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)
