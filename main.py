import json

from flask import Flask, request, current_app, views

from src.utils import (
    CustomResponse,
    ReadImage,
    ProccessText,
)

app = Flask(__name__)


class ConvertImageView(views.MethodView):
    def post(self):
        image = request.files.get('image', False)

        if not image:
            return CustomResponse({"message": 'Image not found'}, status=404)

        read_image = ReadImage(image).create_image_from_path()
        tesseract_text = read_image.convert_image_to_text()
        proccessed_text = ProccessText(tesseract_text)\
            .clean_text()\
            .normalize_text()\
            .spelling_correction()

        current_app.logger.error(proccessed_text.text)

        return CustomResponse({"message": proccessed_text.text})


app.add_url_rule("/", view_func=ConvertImageView.as_view("ConvertImageView"))