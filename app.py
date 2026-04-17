from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# classes (same jo training me use ki)
classes = ['bcc','mel','nv']

medicine_dict = {
    "mel": "Consult doctor urgently",
    "nv": "Normal mole",
    "bcc": "Use cream + consult doctor"
}

# 🔥 DEMO prediction (random)
def predict(img_path):
    return random.choice(classes)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']

        if file.filename == '':
            return "No file selected"

        path = os.path.join("static", file.filename)
        file.save(path)

        result = predict(path)
        medicine = medicine_dict.get(result, "Consult doctor")

        return render_template('index.html', result=result, medicine=medicine, img=path)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)