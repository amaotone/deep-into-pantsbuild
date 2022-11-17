import random

from fastapi import FastAPI

app = FastAPI()


def roll_dice() -> int:
    return random.randint(1, 6)


@app.get("/")
def index():
    return {"result": roll_dice()}
