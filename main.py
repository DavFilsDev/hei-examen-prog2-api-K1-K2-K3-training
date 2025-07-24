from fastapi import FastAPI
from starlette.responses import Response, JSONResponse


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():
    with open("hello.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(
        content=html_content,
        status_code=200,
        media_type="text/html"
    )
@app.get("/welcome")
def welcome(name: str):
    message = f"Welcome {name}"
    return JSONResponse(content={"message": message}, status_code=200)