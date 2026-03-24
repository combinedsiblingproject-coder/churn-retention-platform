from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Churn Retention API is running"}