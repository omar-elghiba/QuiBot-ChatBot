from fastapi import FastAPI

from src.predict.predict import final_func_1
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



origins = ["*"]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model


class Data(BaseModel):
    question:str



@app.get("/chatbot")
def create_answer(question):
    return final_func_1(question)


# @app.post("/test")
# def create_answer(question:Data):
#     return(question)

# @app.post("/chatbot")
# def create_answer(question: Data):
#     return('heeey')


# import random
# from fastapi import FastAPI, Query
# from pydantic import BaseModel


# # class Question(BaseModel):
# #     question: str

# app = FastAPI()

# @app.post("/chatbot")
# def create_application(question):
#     return question.lower()
