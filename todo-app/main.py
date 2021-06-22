from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todo_list/", response_model=schemas.TodoList)
def create_todo_list(todo_list: schemas.TodoListCreate, db: Session = Depends(get_db)):
    db_todo_list = crud.get_todo_list_by_name(db, email=todo_list.name)
    if db_todo_list:
        raise HTTPException(status_code=400, detail="Name already exists")
    return crud.create_todo_list(db=db, todo_list=todo_list)


@app.get("/todo_list/", response_model=List[schemas.TodoList])
def read_todo_list(db: Session = Depends(get_db)):
    db_todo_list = crud.get_todo_list_all(db)
    if db_todo_list is None:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return db_todo_list


@app.get("/todo_list/{todo_list_id}", response_model=schemas.TodoList)
def read_todo_list(todo_list_id: int, db: Session = Depends(get_db)):
    db_todo_list = crud.get_todo_list(db, todo_list_id=todo_list_id)
    if db_todo_list is None:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return db_todo_list


@app.post("/todo_list/{todo_list_id}/items/", response_model=schemas.Item)
def create_item_for_todo_list(todo_list_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_list_item(db=db, item=item, todo_list_id=todo_list_id)


@app.delete("/todo_list/{todo_list_id}/")
def delete_a_todo_list(todo_list_id: int, db: Session = Depends(get_db)):
    crud.delete_todo_list(db, todo_list_id)
    return {"detail": "TODO Deleted"}


@app.delete("/todo_list/items/{todo_list_item_id}/")
def delete_a_todo_list_item(todo_list_item_id: int, db: Session = Depends(get_db)):
    crud.delete_todo_list_item(db, todo_list_item_id)
    return {"detail": "TODO item Deleted"}


@app.put("/todo_list/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, todo_data: schemas.ItemUpdate, db: Session = Depends(get_db)):
    updated_todo = crud.update_todo_list_item(db, item_id, todo_data)
    return updated_todo


@app.get("/todo_list/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)
