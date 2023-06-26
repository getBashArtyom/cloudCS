from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from loguru import logger

app = FastAPI()

logger.add("/fastapi_app/logs/app.log", rotation="100 MB", compression="zip", backtrace=True, diagnose=True)

pipeline = joblib.load('model/model_pipeline.joblib')

class HouseData(BaseModel):
    sqft_living: int = Field(...)
    grade: int = Field(...)
    view: int = Field(...)
    sqft_above: float = Field(...)
    sqft_living15: int = Field(...)


@app.post('/predict')
def predict_price(data: HouseData):
    input_data = [[data.sqft_living, data.grade, data.view, data.sqft_above, data.sqft_living15]]

    predicted_price = pipeline.predict(input_data)
    logger.info("AAAA")
    return {'predicted_price': int(predicted_price[0])}

@app.get('/predict')
def predict_price_get(sqft_living: int, grade: int, view: int, sqft_above: float, sqft_living15: int):
    data = HouseData(sqft_living=sqft_living, grade=grade, view=view, sqft_above=sqft_above, sqft_living15=sqft_living15)
    logger.info("CCCC")
    return predict_price(data)
