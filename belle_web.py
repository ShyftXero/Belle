


from flask import *
from belle_api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")



@app.route("/")
def index():
    return render_template("index.j2")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
