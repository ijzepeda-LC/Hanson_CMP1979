import pytest
from todo_class import TodoList

def test_add_task():
    todo = TodoList()
    assert todo.add_task("Task 1") == "Task added."
    assert todo.add_task("") == "Task cannot be empty."
    assert len(todo.tasks) == 1

def test_view_tasks():
    # Make some tests to view tasks\
    print("Make some tests to view tasks")

def test_delete_task():
    # Make some tests to delete tasks
    print("Make some tests to delete tasks")

def test_clear_tasks():
    # Make some tests to clear tasks
    print("Make some tests to clear tasks")
