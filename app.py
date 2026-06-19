from fastapi import FastAPI, Form
from starlette.responses import RedirectResponse
import uvicorn

from textsummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

obj = PredictionPipeline()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    return {
        "message": "Please run training separately using python main.py"
    }


@app.post("/predict")
async def predict_route(text: str = Form(...)):
    try:
        prediction = obj.predict(text)

        return {
            "summary": prediction
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)