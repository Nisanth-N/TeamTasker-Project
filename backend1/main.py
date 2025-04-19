from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import auth_router
from database.mongo import db

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace this with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Route
@app.get("/")
async def root():
    return {"message": "FastAPI server running!"}

# MongoDB Test Endpoint
@app.get("/test-mongo")
async def test_mongo():
    try:
        collection_names = await db.list_collection_names()
        return {"collections": collection_names}
    except Exception as e:
        return {"error": str(e)}

# Include Auth Routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
