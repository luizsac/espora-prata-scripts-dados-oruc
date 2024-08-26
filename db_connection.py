"""
Estabelece uma conexão com o banco de dados configurado e a retorna
"""

from pyodbc import connect
from os import getenv


# pega atributos das variáveis de ambiente
server: str = getenv('local-sql-server')
database: str = getenv('local-database')
server_pwd: str = getenv('local-server-pwd')

# cria tupla com os dados de conexão
connection_data: str = (
    "Driver={SQL Server};"
    f"Server={server};"
    f"Database={database};"
    f"PWD={server_pwd};"
)


def get_connection():
    """
    Cria uma conexão com o banco de dados e a retorna
    :return: Connection class
    """
    return connect(connection_data)


# cursor = connection.cursor()
