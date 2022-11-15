import psycopg2

import tools


# 创建连接对象
# psql version = 15


def connect_db():
    try:
        connect = psycopg2.connect(
            database='postgres',
            user='senpai',
            password='114514',
            host='127.0.0.1',
            port='5432'
        )
    except Exception as e:
        # error_logger.error(e)
        tools.erro(e)
    else:
        return connect
    return None


def close_db_connection(connect):
    # 提交执行
    connect.commit()
    # 关闭连接
    connect.close()


if __name__ == '__main__':
    conn = connect_db()
    # 创建游标对象
    cur = conn.cursor()

    cur.execute("select * from person;")
    results = cur.fetchall()
    for r in results:
        print(r)
    # cur.execute(f"INSERT INTO person (person_id, name) VALUES (1,'python');")
    # 关闭游标
    cur.close()
    close_db_connection(conn)
