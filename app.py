from flask import Flask, request, jsonify
from pet_class import PetClassification
import os

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return "No image provided", 400
    
    # Ensure the directory exists
    img_directory = "./input_images"
    if not os.path.exists(img_directory):
        os.makedirs(img_directory)

    image_file = request.files['image']
    img_path = "./input_images/" + image_file.filename
    image_file.save(img_path)

    # Process the image
    pet = PetClassification()
    colors = pet.main(img_path)
    # ! debugging only
    print(colors)

    # Return the results as JSON
    return jsonify(colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
