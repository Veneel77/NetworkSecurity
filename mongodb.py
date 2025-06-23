from urllib.parse import quote_plus
import pymongo

username = quote_plus("veneel77")
password = quote_plus("Veneel77@atlasdb")

uri = f"mongodb+srv://{username}:{password}@cluster0.xwrnqvc.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)

try:
    print("Databases:", client.list_database_names())
except Exception as e:
    print("❌ Connection failed:", e)
