from flask import Blueprint, render_template, request, redirect, url_for
from app.steganography import encode_image, decode_image

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        # Logic to handle image encoding
        pass
    return render_template('encode.html')

@main.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        # Logic to handle image decoding
        pass
    return render_template('decode.html')
