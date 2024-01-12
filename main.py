from fastapi import FastAPI, UploadFile,File
import pandas
import json

app = FastAPI()

@app.post("/")
async def upload(file:UploadFile = File(...)):
    df = pandas.read_csv(file.file).T.to_dict()
    json_data = json.dumps(df)
    return json_data

    # Convert DataFrame to JSON
    #json_data = df.to_json(orient='records')

    # Return the JSON data as the response
    #return {"data": json_data}
