from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv
import google.generativeai as genai
import markdown


# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# FastAPI app setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
def render_markdown(text):
    return markdown.markdown(text)

# AI Agent Functions
def thinker_agent(user_input):
    prompt = f"""You are a Thinker AI. Generate 2–3 creative ideas based on this input:
    {user_input}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def checker_agent(ideas_text):
    prompt = f"""You are a Feasibility Checker AI. Review the ideas below and choose the most technically feasible one:
    {ideas_text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def finisher_agent(checked_idea):
    prompt = f"""You are a Final Answer AI. Present the best idea clearly for the user:
    {checked_idea}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Routes
@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def form_post(request: Request, user_input: str = Form(...)):
    thinker_output = thinker_agent(user_input)
    checker_output = checker_agent(thinker_output)
    final_output = finisher_agent(checker_output)

    return templates.TemplateResponse("form.html", {
        "request": request,
        "user_input": user_input,
        "thinker": render_markdown(thinker_output),
        "checker": render_markdown(checker_output),
        "final": render_markdown(final_output)
    })
if __name__ == "__main__":
    import uvicorn, os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

