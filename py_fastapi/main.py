from typing import Union
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

class Persona(BaseModel):
    name: str

app = FastAPI()
client = OpenAI()

@app.get("/")
async def read_root():
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose a haiku that celebrates the virtues of an introvert."}
    ]
  )

  return completion.choices[0].message


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}


@app.post("/personas/{pid}")
async def create_persona(pid: str, persona: Persona):
    result = {"id": pid}
    print("Hey", persona.name)
    return result
