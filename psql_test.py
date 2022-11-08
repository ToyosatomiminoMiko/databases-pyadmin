import psycopg2
import tools


# 创建连接对象
# psql version = 15

def connect_db():
    try:
        connect = psycopg2.connect(
            database='postgres',
            user='postgres',
            password='19260817',
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

    cur.execute("select * from movie;")
    results = cur.fetchall()
    print(results)
    # cur.execute("INSERT INTO movie (movie_id, movie_title, director, author, actor, submission_date) \
    # VALUES (1, 'python', 'myself', 'yourself', 'himself', current_date);")

    # 关闭游标
    cur.close()
    close_db_connection(conn)
