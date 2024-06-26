import pymongo, mongoengine
from pymongo.server_api import ServerApi

def get_db_connection(url: str, db_name: str):
    try:
        print("before connecting to mongodb")

        # client = pymongo.MongoClient(url, server_api=ServerApi('1'))

        client2 = mongoengine.connect(host=url, db=db_name, server_api=ServerApi('1'))
        
        print("After connecting to mongodb")

        # print(client2)

        print(f"this is the connection from mongoengine: {client2['youtube_db']}")
        print("Successfully connected to mongodb")

        db_name = client2['youtube_db']

        return db_name, client2
    
    except Exception as e:
        print(f"Error Connecting To MongoDB Atlas: {str(e)}")


if __name__ == "__main__":
    get_db_connection()