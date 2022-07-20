# Python dependencies needed
- pandas
- openpyxl

# Steps for database and table creation
- With ofertaExcelToCsv.py and the excel with the courses in the same folder, run the python script with the excel as argv to transform to csv.
- Create the horariosfic database in postgres.
- Use the command '\i pathToSql' for creating the courses table.
- Use the command 'COPY courses(asignatura, nombre_asig, creditos, asig_referenciadas, seccion, descripcion, horario, profesor, sede, cat_paquete, paquete, vacantes) FROM 'pathToCsv' DELIMITER ',' CSV HEADER;' for importing the csv to the courses table.