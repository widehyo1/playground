from fastapi import FastAPI

def create_app():
    app_ = FastAPI()

    return app_

app = create_app()

@app.get("/")
def root():
    return {
        "message": "Hello World",
        "test": "here"
    }

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
