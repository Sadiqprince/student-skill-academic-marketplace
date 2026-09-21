from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text


app=FastAPI(
    title="Student skill and academic assistence marketplace", version="1.0.0",
)

@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "servie":"student-marketplace-api"
    }
    
@app.get("/health/db")
def database_health_check():
    with engine.connect() as connection:
        result=connection.execute(text("SELECT 1"))
        return{
            "status":"ok",
            "database":"connected",
        }
    

@app.get("/sad")
def sad_check():
    
    return{
        "name":"my name is sadiq"
    }