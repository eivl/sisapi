import uvicorn

from app import app

if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='127.0.0.1')
