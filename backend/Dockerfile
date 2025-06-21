FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py import_csv.py titanic_full_data.csv ./

# 啟動時先匯入資料再啟動 Flask
CMD ["sh", "-c", "python import_csv.py && python app.py"]
