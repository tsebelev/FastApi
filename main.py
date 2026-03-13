from fastapi import FastAPI, HTTPException
import uvicorn
from router import router as tasks_router  # Переименовываем для ясности


app = FastAPI(
    title="Апи для подключения к бд PostgreSQL",
    description="Подключаемся к PostgreSQL и получаем данные из таблицы house_sales",
    version="1.0.0"
)

# Подключаем роутер к приложению
app.include_router(tasks_router)



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )