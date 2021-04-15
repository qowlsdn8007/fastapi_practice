import uvicorn

from fastapi import FastAPI
from conn import SQLAlchemy, db
from config import conf
from router import router

def create_app():
    app = FastAPI()
    db.create_database()
    """ Initialize Redis """

    """ Define Middleware """

    """ Define Router """
    app.include_router(router)
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
