from flask import Flask
from config import session_key, app_config, mongo_config, jwt_secret
from Controllers import PageRoutes, ErrorRoutes, GoogleRoutes
from Utilities.OAuths import google
import os


app = Flask(__name__)

# app settings
app.secret_key = session_key
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'
app.config['JSON_SORT_KEYS'] = False


# blueprints init
blueprints = [
    PageRoutes.mod,
    ErrorRoutes.mod,
    GoogleRoutes.mod
]
for bp in blueprints:
    app.register_blueprint(bp)

# oauth
app.register_blueprint(google, url_prefix='/auth')
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

if __name__ == '__main__':
    app.run(host="localhost", port=5010, debug=True)
