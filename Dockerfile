FROM python:3.9

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы проекта
#COPY app /app
#COPY alembic /alembic/
#COPY alembic.ini alembic.ini
COPY requirements.txt ./

# Установите необходимые библиотеки
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]