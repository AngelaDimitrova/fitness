FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY wait-for-it.sh /app/ 
COPY . /app
EXPOSE 8000
CMD ["./wait-for-it.sh", "db:5433", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
