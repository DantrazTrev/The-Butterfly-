from flask import *
from Game import *
from flask_cors import CORS, cross_origin




Gy = dict()
app = Flask(__name__)
CORS(app)
ver="alpha"
# Home page which will redirect to docs currently cause that's there
@app.route('/')
def index():
    return redirect(url_for('docs'))

#404 error henadler with a template from /templates
@app.errorhandler(404)
def err(e):
    return render_template('/error.html')

#Index redirects here
@app.route('/docs')
def docs():
    return render_template('/index.html')

#A wrong call requese homie , So for the first one we give an error
@app.route('/api/game/', methods=['GET'])
def dummy():
    ga = {"status": "The game is running correctly", "Version": ver}
    return respor(ga)

# A game init call request which specifies the name and other things of taht matter
@app.route('/api/game/', methods=['POST'])
def start():
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    if inz["name"] in Gy and Gy[inz["name"]].id!=request.remote_addr:
        return respor({"error": "user already here"})
    try:
        Gy[inz["name"]] = Game(request.remote_addr, inz["complexity"], inz["name"])
    except:
        abort(500, error_message="User already here")
    return respor({"status": "user created","ip":"-","name":inz["name"]})

@app.route('/api/game/<string:id>', methods=['POST'])
def begin(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    Gy[id].start(inz["choices"],inz["charecters"],inz["levels"])
    return respor({"status": "game created","number_of_charecters":len(inz["charecters"]),"number_of_choices":len(inz["choices"])})

# For the game config the api request[POST] data : choices<n,1> confidence
@app.route('/api/game/<string:id>/playconfig', methods=['POST'])
def iconfig(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    print(type(inz['choices']),inz['choices'])
    result = Gy[id].whome(inz["choices"], inz["confidence"])
    return respor(result)


@app.route('/api/game/<string:id>/disc', methods=['POST'])
def disc(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].discu(inz["Name"])
    return respor(result)

@app.route('/api/game/<string:id>/inf', methods=['POST'])
def inf(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].pinf(inz["Name"])
    return respor(result)


@app.route('/api/game/<string:id>/upday', methods=['GET'])
def upday(id):
    result = Gy[id].upday()
    return respor(result)

@app.route('/api/game/<string:id>/unt', methods=['GET'])
def utd(id):
    result = Gy[id].utd()
    return respor({"status":"dayupdated","warning":"This endpoint is not supported" })
@app.route('/api/game/<string:id>/fight', methods=['GET'])
def er(id):
    result = Gy[id].fight()
    return respor(result)


@app.route('/api/game/<string:id>/day', methods=['GET'])
def day(id):
    result = Gy[id].daystat()
    return respor(result)

@app.route('/api/game/<string:id>/me', methods=['GET'])
def me(id):
    result = Gy[id].pstat()
    return respor(result)


@app.route('/api/game/<string:id>/kar/<string:name>', methods=['GET'])
def du(id,name):
    result = Gy[id].cstat(name)
    return respor(result)

@app.route('/api/game/<string:id>/undi/<string:name>', methods=['GET'])
def undie(id,name):
    result = Gy[id].undistancedu(name)
    return respor(result)

@app.route('/api/game/<string:id>/di/<string:name>', methods=['GET'])
def dies(id,name):
    result = Gy[id].distancedu(name)
    return respor(result)

@app.route('/api/game/<string:id>/trusty/<string:name>', methods=['POST'])
def duonly(id,name):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].trusty(name,inz["trust"])
    return respor(result)

#Init callable function else will be set to random
@app.route('/api/game/<string:id>/wholetrusty/<string:name>', methods=['POST'])
def wholes(id,name):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].doawholetrusty(inz["tmatrix"])
    return respor(result)

@app.route('/api/game/<string:id>/rewind', methods=['POST'])
def time(id):
    if not request.json:
        abort(400)
    inz = json.loads(request.data)
    result = Gy[id].rewind(inz["day"])
    return respor(result)

@app.route('/api/game/<string:id>/quit', methods=['GET'])
def wee(id):
      Gy[id].quit()
      return respor({"status":"Simulation Removed"})



def respor(dic):
    resp = jsonify(dic)
    resp.status_code = 200
    return resp



app.run('0.0.0.0')
