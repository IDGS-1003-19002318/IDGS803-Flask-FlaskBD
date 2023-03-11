from db import get_connection

''' try:
    con = get_connection()
    with con.cursor() as cursor:
        cursor.execute('call GetAllAlumnos()')
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
    con.close()
except Exception as ex:
    print(ex) '''
    
''' 
try:
    con = get_connection()
    with con.cursor() as cursor:
        cursor.execute('call GetAlumno(%s)',(1,)) #se para una tupla y en este caso es el id la variable
        resultset = cursor.fetchall()
        #resultset = cursor.fetchone()
        for row in resultset:
            print(row)
    con.close()
except Exception as ex:
    print(ex) '''
    
    
try:
    con = get_connection()
    with con.cursor() as cursor:
        cursor.execute('call AddAlumno(%s,%s,%s)',("nombre","apellidos","correo")) #se para una tupla y en este caso es el id la variable
        
    con.commit()
    con.close()
except Exception as ex:
    print(ex)