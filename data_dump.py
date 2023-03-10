import pymongo
import pandas as pd
import json
from creditcard.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb.
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/UCI_Credit_Card.csv"
DATABASE_NAME="credit"
COLLECTION_NAME="creditdata"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Convert dataframe to json so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted json record to mongodb
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)