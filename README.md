# api_yatube

## Описание
- `api/v1/api-token-auth/` (POST): передаём логин и пароль, получаем токен.
- `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост.
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по `id`.
- `api/v1/groups/` (GET): получаем список всех групп.
- `api/v1/groups/{group_id}/` (GET): получаем информацию о группе по `id`.
- `api/v1/posts/{post_id}/comments/` (GET, POST): получаем список всех комментариев поста с `id=post_id` или создаём новый, указав `id` поста, который хотим прокомментировать.
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по `id` у поста с `id=post_id`.

### Стек: 
```
Python 3.7, Django, DRF.
```

Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/api_yatube.git
cd api_yatube
```

Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```

Ставим зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```

Переходим в папку api_yamdb:
```bash
cd yatube_api
```

Выполняем миграции:
```bash
python manage.py makemigrations reviews
```
```bash
python manage.py migrate
```

Создаем суперпользователя:
```bash
python manage.py createsuperuser
```

Запускаем проект:
```bash
python manage.py runserver
```

### Разработчик проекта
- [Смелов Илья](https://github.com/PivnoyFei)
