from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/', methods=["GET","POST"])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return render_template('photo.html', filename = filename)#filename
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


























# Deep Lizard
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/hello", methods=['POST'])
# def hello():
#     message = request.get_json(force=True)
#     name = message['name']
#     response = {
#         'greeting': 'Hello, ' + name + '!'
#     }
#     return jsonify(response)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=80)

#     # @app.route("/")
#     # def index():
#     #     return "Index!"
