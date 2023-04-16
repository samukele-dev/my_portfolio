from django.urls.converters import StringConverter

class SlugsConverter(StringConverter):
    regex = r'[\w\-\.]+'