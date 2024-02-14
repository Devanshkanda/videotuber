from pymongo import MongoClient
from django.conf import settings


def get_db_connection():

    client = MongoClient(settings.env("MONGODB_URI"))

    return client

if __name__ == '__main__':
    print(settings.MONGODB_URI)
