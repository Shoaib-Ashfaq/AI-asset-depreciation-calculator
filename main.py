import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.routes import assets

# Load the .env file.
load_dotenv()

# App.
app = FastAPI()
app.include_router(assets.router)

# Add CORS middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
