from fastapi import FastAPI, UploadFile,File
import pandas

app = FastAPI()

@app.get("/")
def home():
    return"Hello world"
    
@app.post("/upload")
async def upload(file:UploadFile = File(...)):
    df = pandas.read_csv(file.file).T.to_dict()
    return df
