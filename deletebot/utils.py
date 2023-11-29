import psycopg2
from decouple import config


def init_db() -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS admins ('
                'telegram_id INT PRIMARY KEY);'
                
                'CREATE TABLE IF NOT EXISTS channels ('
                'channel_id VARCHAR(50) PRIMARY KEY,'
                'admin_id INT REFERENCES admins(telegram_id) NOT NULL);')
    conn.commit()
    cur.close()
    conn.close()
