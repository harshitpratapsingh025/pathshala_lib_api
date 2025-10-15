from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.routes.api import register_routes


# Load environment variables
load_dotenv()

def create_app() -> FastAPI:
    
    # Create FastAPI app
    app = FastAPI(
        title="Pathshala library API",
        description="API for the Pathshala library management system",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_app()
register_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )