from fastapi import FastAPI

import uvicorn


database = ['pereforce = hohol']
app = FastAPI()


@app.post('/')
async def create_user(user: str):
    return database.append(user)


@app.get('/{id}')
async def get_user(id: int):
    if id < 0:
        return database
    elif len(database)-1 >= id:
        return database[id]
    return 'Не существует пользователей под введеным id.'


@app.put('/{id}')
async def update_user(id: int, user: str):
    if len(database)-1 >= id:
        database[id] = user
        return database
    return 'Не существует пользователей под введеным id.'


@app.delete('/{id}')
async def delete_user(id: int):
    if len(database)-1 >= id:
        user = database[id]
        del database[id]
        return f'{user} под id {id} удален.'
    return 'Не существует пользователей под введеным id.'


if __name__ == '__main__':
    uvicorn.run('main:app')
