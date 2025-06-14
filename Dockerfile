FROM python:3.12-slim

WORKDIR /app
COPY . .
WORKDIR /app/final_task

RUN pip install --no-cache-dir \
    -r backend/requirements.txt \
    -r frontend/requirements.txt

WORKDIR /app
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "final_task/frontend/app.py"]