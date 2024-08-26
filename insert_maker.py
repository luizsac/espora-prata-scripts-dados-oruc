from csv import reader
import db_connection as dbc


with dbc.get_connection() as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(DEP_ID) FROM DEPARTAMENTO;")
    dep_id = cursor.fetchone()[0]

with open("../../../distinct_prod.csv", "r") as dep_file, open("../../../inserts.sql", "w") as inserts_file:
    dep_csv = reader(dep_file)

    for dep_name in dep_csv:
        dep_id += 1
        inserts_file.write(
            "INSERT INTO DEPARTAMENTO(DEP_ID, DEP_DESCRICAO, DEP_DESCONTO, DEP_COEFICIENTE, DEP_SITUACAO, "
            "DEP_ACESSO_API)\n"
            f"VALUES({dep_id}, '{dep_name[0]}', 0, 1, 'A', 'S');\n\n"
        )
