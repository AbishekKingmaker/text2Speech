
from flask import Flask, Response,request,render_template,jsonify
import pyttsx3
import tempfile
import os


app = Flask(__name__)
@app.route("/")
def index():

    return Response(render_template('frontend.html'))
@app.route("/api/call", methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        # text = request.form['speech']
        data = request.json
        text = data.get('speech')
        language = 'en'
        temp_file_name = tempfile.mktemp(dir='.')
        file_name = temp_file_name[2:]+".mp3"
        engine = pyttsx3.init()

        engine.save_to_file(text, file_name)
        engine.runAndWait()
        name = file_name
    data = {
        "name": name
    }
``````````
    return jsonify(data)
@app.route("/speech/<name>")
def streamaudio(name):

    def generate(name):

        path = "path of current directory"
        fullfilename = os.path.join(path,name)
        with open(fullfilename,"rb") as mp3:
            data = mp3.read(1024)
            while data:
                yield data
                data = mp3.read(1024)
    return Response(generate(name),mimetype="audio/x-mp3")
    # return Response(mytext)

if __name__ == "__main__":

    app.run(debug=True)