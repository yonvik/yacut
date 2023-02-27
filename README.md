# "Укоротитель ссылок YaCut"
## Возможности
- создание коротких ссылок по адресу http://localhost:5000
- переадресация к полной ссылке при переходе по короткой
- взаимодействие с api по адресу http://localhost:5000/api/id/
## Стек
- Python 3.9
- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
## Установка
- git clone git@github.com:yonvik/yacut
- cd yacut
- python -m venv venv
- source venv/scripts/activate
- python -m pip install -r requirements.txt
## Создаём .env файл
- FLASK_APP=yacut
- FLASK_ENV=development
- DATABASE_URI=sqlite:///db.sqlite3
- SECRET_KEY=SECRET_KEY
## Запуск
- flask db upgrade
- flask run

## Автор
[Янковский Андрей](https://github.com/yonvik)
