import os, sys, subprocess, re
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/', methods=["GET","POST"])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename1 = "static/img/" + str(photos.save(request.files['photo']))
        shortname = filename1.rsplit('/', 1)[-1]
        cmd = "sh automate_prediction.sh " + shortname
        # This creates a file prediction.txt in project directory
        os.system(cmd)
        with open('prediction.txt','r') as file:
        	predictString = file.read()
		a = predictString.split(')', 1)[0].replace('(', '').replace(')','')
		b = predictString.split(')', 1)[1].replace('(', '').replace(')','')
        return render_template('photo.html', user_image = filename1, pred1 = a, pred2 = b)
    else:
    	return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
