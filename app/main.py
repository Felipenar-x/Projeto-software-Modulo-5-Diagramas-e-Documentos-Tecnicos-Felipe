from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ParseRequest, ParseResponse
from app.services.java_parser import parse_java_code

app = FastAPI(
    title="DoculA Parser API",
    description="Microsserviço responsável por analisar código-fonte e extrair informações para geração de diagramas UML.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "docula-parser-api"
    }


@app.post("/parse/class", response_model=ParseResponse)
def parse_class(request: ParseRequest):
    parsed_classes = parse_java_code(request.source_code)

    return {
        "classes": parsed_classes
    }