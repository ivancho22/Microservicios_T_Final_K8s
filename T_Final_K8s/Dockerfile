FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the entire app
COPY app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3030"]


 



