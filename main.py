from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import joblib
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from auth import create_access_token, get_user

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#logger.add("/fastapi_app/logs/app.log", rotation="100 MB", compression="zip", backtrace=True, diagnose=True)

pipeline = joblib.load('model/model_pipeline.joblib')

class HouseData(BaseModel):
    sqft_living: int = Field(...)
    grade: int = Field(...)
    view: int = Field(...)
    sqft_above: float = Field(...)
    sqft_living15: int = Field(...)


@app.post('/predict', response_class=HTMLResponse)
def predict_price(request: Request, data: HouseData):
    input_data = [[data.sqft_living, data.grade, data.view, data.sqft_above, data.sqft_living15]]
    predicted_price = int(pipeline.predict(input_data)[0])
    return templates.TemplateResponse("prediction_result.html", {"request": request, "predicted_price": predicted_price})

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/predict')
def predict_price_get(
    request: Request,
    sqft_living: int,
    grade: int,
    view: int,
    sqft_above: float,
    sqft_living15: int,
    #token: str = Depends(get_user)
):
    data = HouseData(
        sqft_living=sqft_living,
        grade=grade,
        view=view,
        sqft_above=sqft_above,
        sqft_living15=sqft_living15
    )
    return predict_price(request, data)