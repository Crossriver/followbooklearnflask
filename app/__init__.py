# flask应用一般保存在名为app的包里
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config #这里导入的是小写的config，就是config类里最后边那个字典
from .main import main as main_blueprint

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


# 传入不同配置名，工厂类启动
def create_app(config_name):
    app = Flask(__name__)
    # 从配置项类加载配置，app.config.from_object()是flask自己的功能函数
    app.config.from_object(config[config_name])
    # 配置项的不同场景init可能要做不同的动作，这里调用一下。
    config[config_name].init_app(app)

    # 启动时注册蓝图，相当于注册路由
    app.register_blueprint(main_blueprint)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)



    return app
