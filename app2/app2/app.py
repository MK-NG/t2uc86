import os
from uuid import uuid4
from flask import Flask, request, render_template, send_from_directory, url_for, redirect


app = Flask(__name__, static_folder="static")




APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
@app.route("/upload")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    #If no path creates path 
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    return render_template("complete.html", image_name=filename)

 

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)


if __name__ == "__main__":
    app.run(port=4555, debug=True)


@app.errorhandler(500)
def server_error(e):
    return render_template('error.html'), 500


@app.route('/about')
def about_us():
        return render_template('about.html', title='About Us')