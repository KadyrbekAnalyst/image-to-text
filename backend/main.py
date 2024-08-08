from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Подключение директории для статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

class Prompt(BaseModel):
    prompt: str

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить доступ для всех доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create-image")
def create_image(prompt: Prompt):
    print(prompt.dict())  # Это поможет увидеть, какие данные приходят на сервер
    # Возвращаем URL для локального изображения
    image_url = "http://localhost:8000/static/images/test.png"
    return {"message": image_url}
