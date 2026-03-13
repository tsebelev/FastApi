from fastapi import APIRouter, HTTPException, status
from db_connect import get_house_sales_db, test_connection

router = APIRouter(
    prefix="/db",
    tags=["Задачи подключения к БД"]
)


@router.get("/")
async def root():
    return {
        "message": "Сервер запущен",
        }


@router.get("/test-connection")
async def test_database_connection():
    """Тестирование подключения к базе данных"""
    result = test_connection()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result


@router.get("/house-sales")
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