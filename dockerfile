FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:888"]
# django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on '127.0.0.1' (115)")
