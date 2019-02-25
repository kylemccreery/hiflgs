from flask import Flask
from flask import request
import multisearch3 as ms3
import json

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def main():
    card = request.args.get('card',"none")
    if card == "none":
        return "No card queried"
    else:
        outString = "<h1>Ideal808<br>"
        outString += "-----------</h1><br>"
        results = ms3.check_ideal808(card)
        if results == []:
            outString += 'None found.<br>'
        else:
            for each_result in results:
                outString += str(each_result)+"<br>"
        outString += "<br><h1>Durdle Zone<br>"
        outString += "-----------</h1><br>"
        results = ms3.check_durdle_zone(card)
        if results == []:
            outString += 'None found.<br>'
        else:
            for each_result in results:
                outString += str(each_result)+"<br>"
        outString += "<h1><br>Da-Planet<br>"
        outString += "-----------</h1><br>"
        results = ms3.check_da_planet(card)
        if results == []:
            outString += 'None found.<br>'
        else:
            for each_result in results:
                outString += str(each_result)+"<br>"
        return outString

@app.route('/api')
def api():
    card = request.args.get('card',"none")
    if card == "none":
        return json.dumps("none")
    else:
        return ms3.wrap_it(ms3.check_all_stores_dict(card))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

