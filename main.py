

from datetime import datetime

from fastapi import FastAPI


app = FastAPI(title="Test")

@app.get("/health-check")
async def health_check():
    date = datetime.now().date()
    time = datetime.now().time()
    test = ""
    return {
        "status": True,
        "timestamp": f"{date} {time}"
    }