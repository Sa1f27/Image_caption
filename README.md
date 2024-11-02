# Image Captioning Flask App

This app uses a Vision Transformer (ViT) with GPT-2 to generate captions for images. Users can upload an image, and the app will display a generated caption.

## Features
- Upload images for captioning
- Displays uploaded image and its generated caption

## Setup

1. **Clone Repository**:
   ```
   git clone [<repo-url>](https://github.com/Sa1f27/Image_caption.git)
   cd <repo-directory>
   ```

2. **Install Dependencies**:
   ```
   pip install flask transformers torch pillow
   ```

3. **Create Upload Folder**:
   ```
   mkdir -p static/uploads
   ```

## Run the App
1. **Start Flask Server**:
   ```
   python app.py
   ```
2. **Open in Browser**:
   Visit `http://127.0.0.1:5001` to use the app.

## Usage
1. Upload an image on the homepage.
2. Receive and view the generated caption.

## Files
- `app.py`: Main Flask application code
- `uploads.html`: Upload page template
- `result.html`: Result page template displaying the caption and image

## Model Details
Uses the [VisionEncoderDecoderModel](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) from Hugging Face's Transformers library.
```
