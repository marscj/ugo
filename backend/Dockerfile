FROM python:latest

RUN mkdir /backend
WORKDIR /backend
COPY . /backend

RUN pip install --upgrade && pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.slave:application"]