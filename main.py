from fastapi import FastAPI, UploadFile,File
import pandas
import json

app = FastAPI()

@app.post("/")
async def upload(user_id: str, file:UploadFile = File(...)):
    try:
        #df = pandas.read_csv(file.file).T.to_dict()
        df = pandas.read_csv(file.file)
        data_list = df.to_dict(orient="records")

        result = {"user_id": user_id, "data": data_list}

        return result

    except Exception as e:
        return {"error": f"An erro accurred: {str(e)}"}

    # Convert DataFrame to JSON
    #json_data = df.to_json(orient='records')

    # Return the JSON data as the response
    #return {"data": json_data}
