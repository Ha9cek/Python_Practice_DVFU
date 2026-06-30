from app.db.db import engine, get_session
from app.db.models import Base
from app.db import crud


def main():
    # создаём таблицы
    Base.metadata.create_all(engine)

    session = get_session()

    # две категории
    fiction = crud.create_category(session, "Художественная литература")
    tech = crud.create_category(session, "Программирование")

    # книги для первой категории
    crud.create_book(session, "Война и мир", "Роман-эпопея Толстого", 1200.0, "", fiction.id)
    crud.create_book(session, "Преступление и наказание", "Роман Достоевского", 950.0, "", fiction.id)
    crud.create_book(session, "Мастер и Маргарита", "Роман Булгакова", 1100.0, "", fiction.id)

    # книги для второй категории
    crud.create_book(session, "Чистый код", "Роберт Мартин", 2500.0, "", tech.id)
    crud.create_book(session, "Python. К вершинам мастерства", "Лучано Рамальо", 3200.0, "", tech.id)
    crud.create_book(session, "Грокаем алгоритмы", "Адитья Бхаргава", 1800.0, "", tech.id)

    session.close()
    print("База данных успешно заполнена.")


if __name__ == "__main__":
    main()