from sqlalchemy import create_engine, text
import pandas as pd
from typing import List, Dict, Any

# Параметры подключения к базе данных
DB_PARAMS = {
    "user": "demo_user",
    "password": "demo_password",
    "host": "samples.mindsdb.com",
    "port": "5432",
    "database": "demo",
    "schema": "demo_data"
}

# Создаем строку подключения
DATABASE_URL = f"postgresql://{DB_PARAMS['user']}:{DB_PARAMS['password']}@{DB_PARAMS['host']}:{DB_PARAMS['port']}/{DB_PARAMS['database']}"

# Создаем engine
engine = create_engine(
    DATABASE_URL,
    connect_args={'options': f'-csearch_path={DB_PARAMS["schema"]}'}
)


def get_house_sales_db(limit: int = 10) -> List[Dict[str, Any]]:
    """Получить данные и таблицы house_sales"""
    try:
        query = f"SELECT * FROM house_sales LIMIT {limit}"
        df = pd.read_sql(query, engine)
        

        for col in df.select_dtypes(include=['datetime64']).columns:
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        return df.to_dict(orient='records')
        
    except Exception as e:
        raise Exception(f"Error reading data: {str(e)}")


# тестирования подключения
def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"status": "connected", "message": "Successfully connected to database"}
    except Exception as e:
        return {"status": "error", "message": str(e)}