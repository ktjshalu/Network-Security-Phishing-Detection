from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kjshalu9:<@password>@cluster0.dsatm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client with TLS settings
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
