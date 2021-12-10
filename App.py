from flask import Flask, request
from flask_cors import CORS
from simplex import optimize

app = Flask(__name__)
CORS(app)


@app.route('/')
def default_route():  # put application's code here
    return 'Optimize pulp LP Problem'

@app.route('/about')
def default_about():  # put application's code here
    return 'App for optimize pulp LP Problem'

@app.route('/api/optimize', methods=['POST'])
def simplex_optimize():  # put application's code here
    # z = [6, 1, 5]
    # rests = [[7, 17, 17, 242],
    #          [16, 5, 1, 329],
    #          [18, 3, 3, 325]]
    # param = {}
    # param['z'] = z
    # param['rests'] = rests
    print(request.data)
    json_data = request.json
    z = json_data["z"]
    rests = json_data["rests"]
    str1 = optimize(z, rests)
    print(str1)
    return str1


if __name__ == '__main__':
    app.run()
