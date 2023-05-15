from flask import Flask, redirect, url_for, request, render_template, send_from_directory
import flask
from core import pic, pdf
from Questgen import main


qe= main.QGen()
PHandle = pic.PicHandler()
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/documentation.html')
def documentation():
    return render_template('docs.html')

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@app.route('/api')
def docs():
    return "Api docs soon"

@app.route("/api/v2")
def api():
    return flask.request.args

@app.route("/api/v3", methods=['GET', 'POST'])
def apiv3():
    if request.method=='POST':
        if request.args['type']=='img':
            data = request.files['file']
            output = {"input_text":PHandle.getText(data),"max_questions":10}
            if 'full' in request.args:
                short_qs = qe.predict_shortq(output)
                mc_qs = qe.predict_mcq(output)
                data = {"text":output,"short_qs":short_qs,"mc_qs":mc_qs}
            else:
                output = {"input_text":PHandle.getText(data),"max_questions":10}
                mc_qs = qe.predict_mcq(output)
                data = {"text":output,"short_qs":{},"mc_qs":mc_qs}
            return data
    else:
        return "This is a POST only end point!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, use_reloader=False)