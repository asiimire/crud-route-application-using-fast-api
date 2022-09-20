"""
define an entry point for running our app
which will be running directly in our fastapi site
"""
import uvicorn

if __name__== "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)

