

from bd import obtener_conexion


def Listar():
    conexion = obtener_conexion()
    lista = []
    with conexion.cursor() as cursor:
        cursor.execute(
            'SELECT usuario.nombre as nombre,usuario.apellido,usuario.edad,usuario.cedula ,usuario.fecha as fecha,usuario.hora FROM crud.usuario ')
        lista = cursor.fetchall()
    conexion.close()
    return lista


def Incertar(nombre, apellido, edad, cedula, fecha, hora):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'INSERT INTO usuario(nombre,apellido,edad,cedula,fecha,hora)VALUES(%s,%s,%s,%s,%s,%s)', (nombre, apellido, edad, cedula, fecha, hora))
    conexion.commit()
    conexion.close()


def buscando(cedula):
    conexion = obtener_conexion()
    usuario = []
    with conexion.cursor() as cursor:
        cursor.execute(
            'SELECT usuario.nombre as nombre,usuario.apellido,usuario.edad,usuario.cedula FROM crud.usuario WHERE cedula=%s', (cedula))
        usuario = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return usuario


def Eliminar(cedula):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('DELETE from usuario Where cedula=%s', (cedula))
    conexion.commit()
    conexion.close()


def edit(cedula):
    conecxion = obtener_conexion()
    usuario = None
    with conecxion.cursor() as cursor:
        cursor.execute(
            'SELECT  usuario.codigo as codigo, usuario.nombre as nombre,usuario.apellido as apellido, usuario.edad as edad FROM crud.usuario  WHERE cedula=%s', (cedula))
        usuario = cursor.fetchone()
    conecxion.close()
    return usuario


def Actualizar(nombre, apellido, edad, codigo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'UPDATE crud.usuario SET nombre=%s,apellido=%s,edad=%s Where codigo=%s', (nombre, apellido, edad,  codigo))

    conexion.commit()
    conexion.close()


def Lista():
    conexion = obtener_conexion()
    lista = []
    with conexion.cursor() as cursor:
        cursor.execute(
            'SELECT usuario.nombre as nombre,usuario.apellido,usuario.edad  FROM crud.usuario ')
        lista = cursor.fetchall()
    conexion.close()
    return lista
