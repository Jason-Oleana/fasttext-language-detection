from fastapi import FastAPI
from starlette.responses import RedirectResponse

from languagedetection import LanguageDetection

import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

# Initialize FastAPI
app = FastAPI()

# load model
langdetect = LanguageDetection()

@app.get("/")
def root():
    response = RedirectResponse(url="/redoc")
    return response

@app.post("/languagedetection")
def LanguageDetection(text: str):
    # get detected_user_language
    results = langdetect.language_classification(text)
    # return predictions
    return results

