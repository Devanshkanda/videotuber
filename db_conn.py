import pymongo, mongoengine

def get_db_connection(url: str, db_name: str):
    try:
        print("before connecting to mongodb")

        client = pymongo.MongoClient(url)

        client2 = mongoengine.connect(host=url, db=db_name)
        
        print("After connecting to mongodb")

        print(client)

        print(f"this is the connection from mongoengine: {client2['youtube_db']}")
        print("Successfully connected to mongodb")

        db_name = client['youtube_db']

        return db_name, client
    
    except Exception as e:
        print(f"Error Connecting To MongoDB Atlas: {str(e)}")


if __name__ == "__main__":
    get_db_connection()