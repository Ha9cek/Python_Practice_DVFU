from app.db.db import get_session
from app.db import crud


def main():
    session = get_session()

    categories = crud.get_categories(session)

    for category in categories:
        print(f"\n=== Категория: {category.title} ===")
        for book in category.books:
            print(f"  - {book.title} | {book.price} руб. | {book.description}")

    session.close()


if __name__ == "__main__":
    main()