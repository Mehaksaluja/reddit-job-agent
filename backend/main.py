from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    This function will run when someone visits the main URL of our app.
    """
    return {"message": "Hello, Reddit Job Hunter Agent is starting up!"}