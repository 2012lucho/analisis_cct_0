import sqlite3
import csv

con = sqlite3.connect("dataset.db")
sqlite = con.cursor()

campos = [
        'id integer', 
        'pais_trabajo varchar(255)',
        'provincia_trabajo varchar(255)', 
        'dedicacion varchar(255)',
        'tipo_contrato varchar(255)', 
        'retiro_bruto float',
        'retiro_neto float', 
        'pagos_dolares varchar(255)', 
        'dolarizado_valor float',  
        'recibes_bonos varchar(255)', 
        'bono_atado_a varchar(255)', 
        'actualizaciones_salarios varchar(255)', 
        'porcentaje_ajuste_acumulado float',
        'ultimo_mes_ajuste varchar(255)', 
        'ingresos_vs_semestre_anterior varchar(255)', 
        'adicionales_salariales varchar(255)',
        'conformidad_ingresos varchar(255)', 
        'trabajo_de varchar(255)', 
        'anios_experiencia integer', 
        'antiguedad_empresa_actual integer', 
        'tiempo_en_puesto_actual varchar(255)',
        'cantidad_personas_a_cargo varchar(255)', 
        'plataformas_utilizadas varchar(255)', 
        'lenguajes_tecnologias_puesto_actual varchar(255)', 
        'frameworks_librerias varchar(255)',  
        'bases_de_datos varchar(255)',
        'qa_testing varchar(255)', 
        'cantidad_personas_orga integer', 
        'modalidad_de_trabajo varchar(255)', 
        'dias_semana_oficina varchar(255)',  
        'recomienda_lugar_trabajo varchar(255)', 
        'uso_ia_trabajo varchar(255)', 
        'salir_seguir_contestando varchar(255)', 
        'maximo_nivel_estudios varchar(255)', 
        'estado_estudios varchar(255)',
        'carrera_estudios varchar(255)',
        'institucion_estudios varchar(255)',
        'salir_seguir_contestando_guardias varchar(255)', 
        'tiene_guardias varchar(255)', 
        'cobro_guardia varchar(255)', 
        'aclarar_numero_ingresado varchar(255)', 
        'salir_seguir_contestando_estudios varchar(255)',
        'edad integer', 
        'genero varchar(255)'
    ]

def crear_base_datos():
    sql = "create table registros_encuesta ("
    for campo in campos:
        sql = sql + campo + ','
    sql = sql[:-1]
    sql = sql + ')'
    print(sql)
    sqlite.execute(sql)

def importar_registros():
    with open("encuesta.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        i = 0
        for data in csvreader:
            if (i!=0):
                sql = 'INSERT INTO registros_encuesta ('
                for campo in campos:
                    field = campo.split(' ')[0]
                    if (field != 'id'):
                        sql = sql + field + ','
                sql = sql[:-1]
                sql = sql + ') VALUES ('

                for data_reg in data:
                    data_reg = data_reg.replace('"', '')
                    sql = sql + '"' +data_reg + '"' + ','
                sql = sql[:-1]
                sql = sql + ')'
                print(sql)
                sqlite.execute(sql)
                con.commit()
            i = i + 1


crear_base_datos()
importar_registros()