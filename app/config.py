from os.path import abspath, dirname, join
from random import sample
from string import ascii_letters, digits

TESTING=True
DEBUG=True
ENV="development"
SECRET_KEY = "".join(sample(ascii_letters + digits, 32))
BASEDIR = abspath(dirname(__file__))

DATABASE_PATH = join(BASEDIR, "db.sqlite")
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(DATABASE_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False