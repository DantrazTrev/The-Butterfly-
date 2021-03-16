from flask import *
from Game import *

Gy = dict()

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('docs'))


@app.errorhandler(404)
def err(e):
    return render_template('/error.html')


@app.route('/docs')
def docs():
    return render_template('/index.html')


@app.route('/api/game/', methods=['GET'])
def dummy():
    ga = {"message": "Wrong request,please refer to the docs", "URL": "idk"}
    return respor(ga)


@app.route('/api/game/', methods=['POST'])
def start():
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    if inz["name"] in Gy:
        return respor({"error": "user already here"})
    try:
        Gy[inz["name"]] = Game(inz["id"], inz["complexity"], inz["name"])
    except:
        abort(500, error_message="User already")
    return respor({"status": "game created"})


@app.route('/api/game/<string:id>/playconfig', methods=['POST'])
def iconfig(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].whome(inz["choices"], inz["Confidence"])
    return respor(result)


@app.route('/api/game/<string:id>/disc', methods=['POST'])
def disc(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].dsic(inz["Name"])
    return respor(result)


@app.route('/api/game/<string:id>/upday', methods=['GET'])
def upday(id):
    result = Gy[id].upday()
    return respor(result)




def respor(dic):
    resp = jsonify(dic)
    resp.status_code = 200
    return resp



app.run('0.0.0.0', debug=True)
