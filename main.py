from fastapi import FastAPI, UploadFile,File
import pandas

app = FastAPI()

@app.post("/")
async def upload(file:UploadFile = File(...)):
    df = pandas.read_csv(file.file)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Return the JSON data as the response
    return {"data": json_data}
