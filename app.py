from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image
from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model from nlp
model_name = "nlpconnect/vit-gpt2-image-captioning"

try:
    model = VisionEncoderDecoderModel.from_pretrained(model_name)
    feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_caption = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_caption

@app.route('/')
def home():
    return render_template('uploads.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        caption = generate_caption(file_path)
        return render_template('result.html', caption=caption, image_path=file_path)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
