from fastapi import FastAPI
from app.anonymize.anonymize import router

app = FastAPI()
app.include_router(router)

@app.get('/')
async def main():
    return {'message': 'Welcome to Anonymizer!'}