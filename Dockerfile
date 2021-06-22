FROM python:3.8.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 80

WORKDIR /Fast-todo
COPY . /Fast-todo

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE $PORT

CMD ["uvicorn", "todo-app.main:app", "--host", "0.0.0.0", "--port", "80"]