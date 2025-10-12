import os, sys
from datetime import datetime
from zoneinfo import ZoneInfo
import pymysql

def main():
    host = os.getenv("DB_HOST", "mysql.sa-p5.svc.cluster.local")
    port = int(os.getenv("DB_PORT", "3306"))
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    dbname = os.getenv("DB_NAME", "cron_db")
    carnet = os.getenv("CARNET", "SIN_CARNE")

    tz = ZoneInfo("America/Guatemala")
    now_local = datetime.now(tz).replace(microsecond=0)

    conn = pymysql.connect(host=host, port=port, user=user, password=password, autocommit=True)
    try:
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
            cur.execute(f"USE {dbname}")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cron_runs (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  carnet VARCHAR(32) NOT NULL,
                  executed_at TIMESTAMP NOT NULL,
                  tz VARCHAR(64) NOT NULL
                )
            """)
            cur.execute(
              "INSERT INTO cron_runs (carnet, executed_at, tz) VALUES (%s, %s, %s)",
              (carnet, now_local.strftime("%Y-%m-%d %H:%M:%S"), "America/Guatemala")
            )
        print("OK: insert realizado")
    finally:
        conn.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
        sys.exit(1)