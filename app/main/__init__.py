from flask import Blurprint
main = Blurprint('main',__name__)
from . import views,errors

