import json

from flask import Flask, request, Response, views

from src.utils import CustomResponse, ReadImage

app = Flask(__name__)


class ConvertImageView(views.MethodView):
    def post(self):
        image = request.files('image', False)

        if not image:
            return CustomResponse({"message": 'Image not found'}, status=404)

        read_image = ReadImage(image).create_image_from_path()

        return CustomResponse({"message": read_image.convert_image_to_text()})


app.add_url_rule("/", view_func=ConvertImageView.as_view("ConvertImageView"))