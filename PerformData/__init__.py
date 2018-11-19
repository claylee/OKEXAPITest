from flask import Blueprint

performData = Blueprint("performData", __name__,template_folder='/templates')
print("picview blueprint name:",__name__)

from PerformData import views, errors
