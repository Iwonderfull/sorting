import psycopg2 as psql  # Так создаются алиасы (короткое прозвище) на подключенные модули

connection = psql.connect(
    dbname="zoo",
    user="zookeeper",
    password="cage_lock",
    host="localhost",
)
cursor = connection.cursor()
cursor.execute(
    """\
CREATE TABLE IF NOT EXISTS test (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Animal text,
    Class text,
    Count int
);
"""
)

cursor.execute(
    """\
INSERT INTO test (Animal, Class, Count) VALUES 
('giraffe', 'Mammalia', 13000),
('Weasel', 'Mammalia', 8000),
('gopher', 'Mammalia', 13000);
"""
)

connection.commit()
cursor.execute(
    """\
SELECT * FROM test;
"""
)
for item in cursor.fetchall():
    print("id: {:2} Animal: {:7} Class: {} Count: {}".format(*item))

cursor.execute(
    """\
    TRUNCATE test CASCADE;
"""
)
connection.commit()
cursor.close()
connection.close()
