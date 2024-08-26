from _csv import reader
from csv import reader


with open("../../../distinct_prod.csv", "r") as dep_file, open("../../../distinct_prod_desc.csv", "r") as pro_file, open("../../../updates.sql", "w") as updates_file:
    dep_csv = reader(dep_file)
    pro_csv = reader(pro_file)

    for dep_name, pro_desc in zip(dep_csv, pro_csv):
        updates_file.write(
            "UPDATE PRODUTO\n"
            f"SET DEP_ID = (SELECT DEP_ID FROM DEPARTAMENTO WHERE DEP_DESCRICAO = '{dep_name[0]}')\n"
            f"WHERE PRO_DESCRICAO LIKE '{pro_desc[0]} %';\n\n"
        )
