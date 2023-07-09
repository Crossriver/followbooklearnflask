# 用于存储配置
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# 用配置类实现配置
class Config:
    # os.environ.get就是
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    BOOTSTRAP_SERVE_LOCAL=True # 采用本地静态文件
    # 邮件设置
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS=False


    @staticmethod
    def init_app(app):
        pass

# 下面这三个类都继承了主类config，然后可以在各自场景配置不同的数据库，比如生产数据库和测试数据库，开发数据库
class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

# 指向三个配置场景
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig #默认启动调测状态
}

if __name__=="__main__":
    for k,v in config.items():
        print(k,v)
