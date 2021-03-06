import os
basedir = os.path.abspath(os.path.dirname(__file__))

mysqlpsd=os.environ.get('mysqlpsd')


SECRET_KEY = os.urandom(24)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
WTF_CSRF_ENABLED = False
DEBUG=True
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                          'mysql+pymysql://root:'+mysqlpsd+'@localhost:3306/todo'
