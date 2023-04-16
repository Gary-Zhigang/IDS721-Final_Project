import os
from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["ALLOWED_EXTENSIONS"] = {"jpg", "jpeg", "png", "gif"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

def load_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img = np.array(img) / 255.0
    return np.expand_dims(img, axis=0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return redirect(url_for("result", filename=file.filename))

    return render_template("index.html")

@app.route("/result/<filename>")
def result(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    img = load_image(filepath)
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    predictions = model.predict(img)
    labels = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
    return render_template("result.html", filename=filename, labels=labels)

if __name__ == "__main__":
    app.run(debug=True)
