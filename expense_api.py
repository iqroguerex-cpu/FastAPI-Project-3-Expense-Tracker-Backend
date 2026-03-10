from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

EXPENSES = [
    {"id":1,"title":"Groceries","amount":52.40,"category":"food","date":"2026-04-10"},
    {"id":2,"title":"Taxi Ride","amount":18.75,"category":"transport","date":"2026-07-09"},
    {"id":3,"title":"Movie Ticket","amount":12.00,"category":"entertainment","date":"2026-02-08"},
    {"id":4,"title":"Coffee","amount":4.50,"category":"food","date":"2026-03-08"},
    {"id":5,"title":"Internet Bill","amount":45.00,"category":"utilities","date":"2026-08-05"}
]

@app.get("/expenses")
async def get_expenses():
    return EXPENSES


@app.get("/expenses/{expense_id}")
async def get_expense_by_id(expense_id: int):
    for expense in EXPENSES:
        if expense.get("id") == expense_id:
            return expense
    return "Expense Not Found"


@app.post("/expenses/create_expense")
async def create_expense(expense = Body()):
    EXPENSES.append(expense)
    return "Expense Added Successfully"


@app.put("/expenses/update_expense/{expense_id}")
async def update_expense_by_id(expense_id: int, updated_expense = Body()):
    for i in range(len(EXPENSES)):
        if EXPENSES[i].get("id") == expense_id:
            updated_expense["id"] = expense_id
            EXPENSES[i] = updated_expense
            return "Expense Updated Successfully"
    return "Expense Not Found"


@app.delete("/expenses/delete_expense/{expense_id}")
async def delete_expense(expense_id: int):
    for i in range(len(EXPENSES)):
        if EXPENSES[i].get("id") == expense_id:
            EXPENSES.pop(i)
            return "Expense Deleted Successfully"
    return "Expense Not Found"
