from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_hello(firstname : str = "firstname", lastname : str = "lastname"):
  return f'Hello {firstname} {lastname}'