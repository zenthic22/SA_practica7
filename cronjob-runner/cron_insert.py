import os, sys, time
from datetime import datetime
from zoneinfo import ZoneInfo
import pymysql
from pymysql import OperationalError

DB_HOST = os.getenv("DB_HOST", "mysql.sa-p5.svc.cluster.local")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "cron_db")
CARNET  = os.getenv("CARNET", "201807169")

TZ_NAME = "America/Guatemala"
tz = ZoneInfo(TZ_NAME)

def connect_with_retries(max_tries=10, delay=3):
    for i in range(1, max_tries + 1):
        try:
            return pymysql.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASS,
                autocommit=True,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.Cursor,
            )
        except OperationalError as e:
            print(f"[{i}/{max_tries}] DB no disponible: {e}", file=sys.stderr)
            time.sleep(delay)
    raise SystemExit("No se pudo conectar a la DB después de varios intentos")

def main():
    now_local = datetime.now(tz).replace(microsecond=0)
    conn = connect_with_retries()
    try:
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
            cur.execute(f"USE `{DB_NAME}`")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cron_events (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    carnet VARCHAR(20) NOT NULL,
                    message VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute(
                "INSERT INTO cron_events (carnet, message, created_at) VALUES (%s, %s, %s)",
                (CARNET, "cron ok", now_local.strftime("%Y-%m-%d %H:%M:%S"))
            )
        print("OK: insert realizado en cron_events")
    finally:
        conn.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
        sys.exit(1)