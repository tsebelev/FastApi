from fastapi import FastAPI, HTTPException
import uvicorn
from db_connect import get_house_sales_db, test_connection

app = FastAPI(
    title="Апи для подключения к бд PostgreSQL",
    description="Подключаемся к PostgreSQL и получаем данные из таблицы house_sales",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Сервер запущен",
        }


@app.get("/test-connection")
async def test_database_connection():
    """Тестирование подключения к базе данных"""
    result = test_connection()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result


@app.get("/house-sales")
async def get_house_sales(limit: int = 10):
    """ Получить данные из таблицы house_sales количество записей (по умолчанию 10) """
    try:
        data = get_house_sales_db(limit)
        return {
            "total_rows": len(data),
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )