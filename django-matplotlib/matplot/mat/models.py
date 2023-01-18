from django.db import models
from django_matplotlib import MatplotlibFigureField
from .figures import my_figure

class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')