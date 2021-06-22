from sqlalchemy.orm import Session
from . import models, schemas


def get_todo_list(db: Session, todo_list_id: int):
    return db.query(models.TodoList).filter(models.TodoList.id == todo_list_id).first()


def get_todo_list_all(db: Session):
    return db.query(models.TodoList).all()


def get_todo_list_by_name(db: Session, email: str):
    return db.query(models.TodoList).filter(models.TodoList.name == email).first()


def create_todo_list(db: Session, todo_list: schemas.TodoListCreate):
    db_todo_list = models.TodoList(name=todo_list.name)
    db.add(db_todo_list)
    db.commit()
    db.refresh(db_todo_list)
    return db_todo_list


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_todo_list_item(db: Session, item: schemas.ItemCreate, todo_list_id: int):
    db_item = models.Item(**item.dict(), todo_list_id=todo_list_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_todo_list(db: Session, todo_list_id: int):
    todo_list = db.query(models.TodoList).filter(models.TodoList.id == todo_list_id).first()
    db.delete(todo_list)
    db.commit()


def delete_todo_list_item(db: Session, todo_list_item_id: int):
    todo_list_item = db.query(models.Item).filter(models.Item.id == todo_list_item_id).first()
    db.delete(todo_list_item)
    db.commit()


def update_todo_list_item(db: Session, item_id: int, todo_data: schemas.ItemUpdate):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    item.title = todo_data.title
    item.description = todo_data.description
    db.commit()
    db.refresh(item)
    return item
