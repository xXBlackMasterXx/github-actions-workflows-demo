from fastapi import FastAPI

app = FastAPI(
    title="Traviak API",
    description="API for Traviak",
    version="0.0.1",
    contact={
        "name": "Traviak",
        "url": "https://traviak.com",
        "email": "info@traviak.com"
    }

)

@app.get("/")
def read_root():
    return {"Message": "Welcome to Traviak API"}