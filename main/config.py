import os

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://volhmwzchxljyz:d600c60f51b6b8148ab697d2e02c98c9b93cfc4f2ac74373c5c342f62800447c@ec2-34-233-187-36.compute-1.amazonaws.com:5432/dbltiienqrsb2k')
    