from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.openai_client import query_model  # Make sure this function is async

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, question: str = Form(...)):
    answer = await query_model(question)  # Await the async function
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question,
        "answer": answer
    })
