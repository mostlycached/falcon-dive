from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import input

app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(input.router, prefix="/api", tags=["Input"])

# Example route
@app.get("/api/health")
async def health_check():
    return {"status": "OK", "message": "FastAPI is running"}