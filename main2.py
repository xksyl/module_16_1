from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page():
    return {'message': 'Главная страница'}

@app.get("/user/admin")
async def us_ad() -> str:
    return (f"Вы вошли как администратор")


@app.get("/user/{user_id}")
async def user_id_page(user_id) -> str:
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user/{user_name}/{age}")
async def us_age(user_name: str = 'Egor', age: int = 20) -> str:
    return (f"Информация о пользователе. Имя: {user_name}, Возраст: {age}")







