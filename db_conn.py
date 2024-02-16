import pymongo
from django.conf import settings


def get_db_connection(url):
    try:
        print("before connecting to mongodb")

        client = pymongo.MongoClient(url)
        
        print("After connecting to mongodb")

        print(client)

        print("Successfully connected to mongodb")
        
        my_db = client['testDB']
    
    except Exception as e:
        print(f"Error Connecting To MongoDB Atlas: {str(e)}")


if __name__ == "__main__":
    get_db_connection()