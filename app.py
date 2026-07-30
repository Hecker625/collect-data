from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/uploadImage', methods=["POST"])
def uploadImage():
    img = request.files['image']
    img.save('face.png')
    return 'OK', 200

@app.route("/uploadData", methods=["POST"])
def uploadData():
    data = request.files["data"]
    data.save("data.txt")
    return "OK", 200

@app.route("/downloadFaceImage")
def downloadFace():
    return send_file("face.png", as_attachment=True)

@app.route("/downloadComputerData")
def downloadComputerData():
    return send_file("data.txt", as_attachment=True)

app.run(host="0.0.0.0", port=80)
