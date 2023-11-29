import psycopg2
from decouple import config


def adjust(query: str) -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()