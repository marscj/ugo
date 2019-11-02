FROM python:latest

RUN mkdir /backend
WORKDIR /backend
COPY . /backend

RUN pip install --upgrade -i http://mirror.youweb.com/pypi/simple
RUN pip install -r requirement.txt -i http://mirror.youweb.com/pypi/simple

EXPOSE 8000

# CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.slave:application"]