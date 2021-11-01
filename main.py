import os
from PIL import Image
import pytesseract
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/process/<language>", methods=['POST'])
def process_image(language):
    assert language == request.view_args['language']
    file = request.files['file']
    path = os.path.join("images/", file.filename)
    file.save(path)
    im = Image.open(path)
    text = pytesseract.image_to_string(im, lang=language)
    os.remove(path) # clean up deleting the image
    return text
    # return "existo subio"


# # print(text)
# with open(  "text_file/salida.txt", "w") as text_file:
#     text_file.write(text)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)