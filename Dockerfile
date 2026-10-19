FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt .
COPY mortgage.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда, которая выполнится при запуске контейнера
CMD ["python", "mortgage.py"]