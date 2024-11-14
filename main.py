from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
from fastapi.security import HTTPBasicCredentials, HTTPBasic

app = FastAPI()
app.title = "FastAPI SENA"
app.version = "1234"


security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username == correct_username and credentials.password == correct_password:
        return credentials.username
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )


class UserSchema(BaseModel):
    id_usuario: Optional[str] = None
    nombre: str

@app.get("/users/{id}", tags=['Users'])
def users(id: int):
    return {"message": f"Hello user {id}"}

@app.put("/", tags=['Home'])
def update():
    return "Updated"

@app.post("/", tags=['Home'])
def create(user: UserSchema):
    return {"message": "User created", "user": user}

@app.delete("/", tags=['Home'])
def delete():
    return "Deleted"

@app.get("/", tags=["Home"], response_class=HTMLResponse)
def home():
    return """
    <html>
         <head>
              <title>Home Page</title>
         </head>
         <body>
              <h1>Hello FastAPI Sena</h1>
        </body>
    </html>
    """
