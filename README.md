1. Создать и активировать виртуальное окружение:

   python3 -m venv venv
   source venv/bin/activate

2. Установить зависимости:

   pip install -r requirements.txt

3. Создать файл `.env` в корне проекта с параметрами БД:

   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=octagon_db
   DB_USER=octagon
   DB_PASSWORD=12345

4. Заполнить базу начальными данными:

   python -m app.init_db

5. Запустить API:

   uvicorn app.main:app --reload

6. Открыть документацию: http://127.0.0.1:8000/docs