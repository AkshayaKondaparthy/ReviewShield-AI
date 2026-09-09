from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.predict import router as predict_router
from app.routes.analytics import router as analytics_router
from app.routes.reports import router as reports_router

app = FastAPI(
    title="ReviewShield AI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Later you can replace "*" with your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(predict_router)
app.include_router(analytics_router)
app.include_router(reports_router)

@app.get("/")
def root():
    return {
        "message": "ReviewShield AI Backend Running"
    }