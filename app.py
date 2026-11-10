from fastapi import FastAPI,HTTPException
from model import Book
import repository

app = FastAPI()

# HOME 
@app.get("/")
def home():
    return {"message":"Successfully logged with the FastAPI Application"}

# CREATE
@app.post("/book")
def create_books(book:Book):
    result = repository.create_books(book)
    if result is not None:
        return {"message":"Successfully created the books",
                "book": result
                }
    raise HTTPException(status_code = 404, detail = "book not found")

# READ
@app.get("/book")
def get_books():
    result = repository.get_books()
    if result is not None:
        return {
                "message":"Successfully fetched the books",
                "book": result
                }
    raise HTTPException(status_code = 404, detail = "book not found")

# UPDATE
@app.put("/book/{id}")
def update_books(id:int, book:Book):
    result = repository.update_books(id,book)
    if result is not None:
        return {
            "message":"Successfully fetched the books",
            "book": result
                }
    raise HTTPException(status_code = 404, detail = "book not found")

# DELETE
@app.delete("/book/{bookName}")
def delete_books(bookName:str):
    result = repository.delete_books(bookName)
    if result is not None:
        return {
                "message":"Successfully deleted the book",
                "book": result
                }
    raise HTTPException(status_code = 404, detail = "book is not found")