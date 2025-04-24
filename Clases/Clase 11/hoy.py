import duckdb
import pandas as pd

# Cargar la hoja de Excel
df = pd.read_excel("dengue-zika-ppt.xlsx", sheet_name="Hoja 1")


con = duckdb.connect()
con.register("casos", df)

# Ver columnas con "*sin dato*"
res1 = con.execute("""
SELECT DISTINCT grupo_edad_id 
FROM casos
WHERE grupo_edad_id = '*Sin Especificar*'
""").fetchdf()

#print(res1)

# Filas con IDs geográficos igual a 0 (posiblemente inválidos)
res2 = con.execute("""
SELECT *
FROM casos
WHERE departamento_id = 0 OR provincia_id = 0
""").fetchdf()

#print(res2)

# Duplicados exactos
res3 = con.execute("""
SELECT *, COUNT(*) as repeticiones
FROM casos
GROUP BY ALL
HAVING COUNT(*) > 1
""").fetchdf()

#print(res3)

# Registros de edad on grupos no especificados 

res4 = con.execute("""
SELECT *
FROM casos
WHERE grupo_edad_id IS NULL or grupo_edad_id = 'Sin Especificar'
""").fetch_df()

res5 = con.execute("""
SELECT COUNT(*) AS grupo_sin_edad
FROM casos
WHERE grupo_edad_id IS NULL or grupo_edad_id = 'Sin Especificar'
""").fetch_df()

print(res4, '\n')
print(res5)