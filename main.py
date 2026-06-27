from fastapi import FastAPI

app = FastAPI(title="Product Price Tracker API")


@app.get("/")
def root():
    return {"message": "Product Price Tracker API is running"}
