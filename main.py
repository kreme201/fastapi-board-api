import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.application:app", port=8001, log_level="info", reload=True)
