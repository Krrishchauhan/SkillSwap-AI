from fastapi import FastAPI
from database import engine
from models import Base
from models import User
from database import SessionLocal
from auth import hash_password

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "SkillSwap AI Backend Running 🚀"}
@app.get("/about")
def about():
    return {
        "app": "SkillSwap AI",
        "version": "1.0",
        "developer": "Krrish"
    }
@app.get("/profile")
def profile():
    return {
        "name": "Krrish",
        "role": "Software Developer",
        "project": "SkillSwap AI"
    }
@app.post("/register")
def register(name: str, email: str, password: str):
    db = SessionLocal()
    hashed_password = hash_password(password)

    new_user = User(
        name=name,
        email=email,
        password=hashed_password
    )
    

    db.add(new_user)
    db.commit()

    db.close()

    return {
        "message": "User Registered Successfully"
    }
@app.get("/users")
def get_users():
    db = SessionLocal()

    users = db.query(User).all()

    return users
@app.get("/test-hash")
def test_hash():
    return {
        "hash": hash_password("123456")
    }