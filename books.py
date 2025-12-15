from fastapi import Body, FastAPI

app = (FastAPI())

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{title}")
async def read_book(title:str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book
        else:
            return {"error":"book not found"}
    return None

@app.get("/books/")
async def read_category_book(category:str):
    return_books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            return_books.append(book)

    return return_books

# post request

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


# put

@app.put("/books/update_book")
async def update_book(new_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == new_book.get('title').casefold():
            BOOKS[i] = new_book

#delete
@app.delete("/books/delete_book/{title}")
async def delete_book(title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)
            break


#get all books from specific author

@app.get("/books/author/{author}")
async def read_all_books_by_author(author:str):
    return_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            return_books.append(book)

    return return_books