import sys
import psycopg2
from sshtunnel import SSHTunnelForwarder
import xmltodict
import codecs

handle = codecs.open("C:/Users/kharlamov/Desktop/Работа/files/config.xml", "r", "utf_8_sig")
content = handle.read()
data = xmltodict.parse(content)


class Connection():
    print("Список доступных серверов:\n1.omega\n2.beta\n3.kalmikia\n4.irkutsk\n5.bashkiria\n6.altai")

    def __init__(self):
        self.server_name = str(input())

    def connect_SSH(self):
        print(data['server'][self.server_name]['ssh']['host'])
        # Подключаемся к серверу
        try:
            server = SSHTunnelForwarder(
                (str(data['server'][self.server_name]['ssh']['host']),
                 int(data['server'][self.server_name]['ssh']['port'])),
                ssh_username=str(data['server'][self.server_name]['ssh']['user']),
                ssh_password=str(data['server'][self.server_name]['ssh']['password']),
                remote_bind_address=('localhost', 5432),
                local_bind_address=('localhost', 22)
            )

            server.start()
            print("Подключились к серверу")

        except EOFError as e:
            print(e)
            print("Не удалось подключиться к серверу")
            sys.exit()

        return server

    def connect_DB(self, server):
        # Подключаемся к БД

        print(self.server_name)

        try:
            conn = psycopg2.connect(dbname=str(data['server'][self.server_name]['db']['dbname']),
                                    user=str(data['server'][self.server_name]['db']['user']),
                                    password=str(data['server'][self.server_name]['db']['password']),
                                    host=server.local_bind_host,
                                    port=server.local_bind_port)
            # Проверка на работоспособность запросов в БД
            cur = conn.cursor()
            cur.execute("select * from organization_ limit 1")
            count = cur.fetchall()
            print("Обращение к БД успешно")

        except EOFError as e:
            print(e)
            print("Не удалось подключиться к БД")
            server.stop()
            sys.exit()

        return conn
