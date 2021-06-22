# FastAPI-todo

Before running the app assuming that **python 3.8.xx** is installed on development machine

1. Create virtual enviroment with python3.8.xx
```shell
$ python3.8 -m venv envname
```
2. Activate the virtual enviroment
```shell
$ source envname/bin/activate
```
3. Install requisite packages:
```shell
$ sh scripts/install_requirements.sh
```
4. Run FAST API:
```shell
$ uvicorn todo-app.main:app --reload
```
5. FAST API DOCS Url:
```
http://127.0.0.1:8000/docs
```
