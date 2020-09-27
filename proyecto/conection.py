import mysql.connector 
from proyecto.users import user
from datetime import date
from proyecto import login_manager

@login_manager.user_loader
def load_user(user_id):
  conn=conexion()
  where="idUsuario="+user_id
  #Se crea el objeto usuario y se almacena en la variable usuario
  usuario=conn.select("*","usuarios",where,"1")
  return usuario



class conexion:

    def __init__(self):
      self.ht="localhost"
      self.db="idoctorv4"
      self.usuario="root"
      self.password=""

      self.conexion = mysql.connector.connect(host=self.ht,
                                             database=self.db,
                                             user=self.usuario,
                                             password=self.password)

#BANDERA: 1.- PARA SELECT, 2.-PARA INSERT o Hacer Commit

    def ejecutar_query(self, query,bandera):
      cursor=self.conexion.cursor()
      try:
        #print("BANDERA ",query)
        cursor.execute(query)
        if bandera == "2":
          #print("QUERY INSERT")
          self.conexion.commit()
          return True
        else:
          #print("QUERY SELECT")
          return cursor
      except self.conexion.Error as err:
        print("Something went wrong: {}".format(err))

# METODO SELECT
#  columna: atributo usado de referencia
#  where: condicion 2 posibles casos("contraseña = 123 and email =uaq@gmail.com" ó "1")
#  tabla: tabla a la que se hara la consulta
#  bandera: 1.- retorna toda la fila de la bd (usado para instanciar el objeto User)
#                                             "columna = *" obligatoriamente
#           2.- retorna todos los registros
#           3.- retorna un unico registro si existe (usado para obtener contraseña hasheada)
        

    def select(self, columna,tabla, where,bandera):

      query=("SELECT "+columna+" from "+tabla+" WHERE "+where)

      if bandera == "1":
        cursor= self.ejecutar_query(query,"1")
        data = cursor.fetchone()
        cursor.close()
        usuario=user(data[0],data[1],data[2],data[3],data[4],data[5])
        return usuario
      elif bandera == "2":
        cursor= self.ejecutar_query(query,"1")
        data = cursor.fetchall()
        cursor.close()
        return data
      elif bandera == "3":
        cursor= self.ejecutar_query(query,"1")
        resultado = cursor.fetchone()
        data= str(resultado[0])
        return data
      elif bandera == "4":
        query="SELECT id, nombre_color FROM tela"
        cursor= self.ejecutar_query(query,"1")
        data = cursor.fetchall()

        return data

    def insert_modelo(self,tipo_prenda,peso_kg,precio, tela, genero, nombre,cantidad):
    
      query="INSERT INTO prenda (tipo_prenda,peso_kg,precio,id_tela,genero,nombre,cantidad) ""VALUES ('%s',%.2f,%.2f,%i,'%s','%s',%i)"%(tipo_prenda,peso_kg,precio,tela,genero,nombre,cantidad)
      self.ejecutar_query(query,"2")


    def insert_usuarios(self, nombre, apellidos, password, email, id_tipo):

      query=('INSERT INTO usuarios (nombreUsuario, apellidoUsuario, emailUsuario, password, idTipo) '
              f'VALUES ("{nombre}", "{apellidos}","{email}","{password}","{id_tipo}")')
      print("QUERY--------------------------",query)
      self.ejecutar_query(query,"2")
      
    def insert_tela(self, nombre_color, peso):

      query="INSERT INTO tela (nombre_color, peso_kg)VALUES ('%s',%3f)"%(nombre_color,peso)
      self.ejecutar_query(query,"2")

    def select_modelos_ropa(self):
      query="SELECT p.id, p.tipo_prenda, p.peso_kg, p.precio,t.Nombre_color, p.genero, p.nombre, p.cantidad FROM `prenda` as p INNER join tela as t where p.Id_tela = t.Id"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pedidos(self):
      query="SELECT P.id,p.estatus, p.total, p.fecha, p.cantidad,pr.Nombre, c.Nombres,c.Apellido_Materno from pedidos as p inner join prenda as pr INNER join clientes as c WHERE pr.Id = p.Id_prenda and c.Id = p.Id_cliente"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_1_pedido(self,idPedido):
      query="SELECT p.id,p.estatus, p.total, p.fecha, p.cantidad,pr.Nombre, c.Nombres,c.Apellido_Materno,p.Id_Prenda from pedidos as p inner join prenda as pr INNER join clientes as c WHERE pr.Id = p.Id_prenda and c.Id = p.Id_cliente and p.id ="+idPedido+""
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data
    def select_telas(self):
      query="SELECT * FROM Tela"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def obtener_idPedido(self,idPedido):
      query="SELECT estatus from Pedidos where Id ="+idPedido+""
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def delete(self,tabla,where):

      query=("DELETE FROM " +tabla +" WHERE "+where)
      print("QUERY DELETE",query)
      result= self.ejecutar_query(query,"2")
      return result

    def update_estatus_pedido(self,idPedido,estatus):

      query="UPDATE Pedidos SET estatus = "+ estatus+" WHERE id ="+idPedido+""
      result= self.ejecutar_query(query,"2")

      return result
    def update_telas(self,idTela,color_tela, peso):
      query="UPDATE Tela SET nombre_color = '%s', peso_kg = %3f WHERE id = %s "%(color_tela,peso,idTela)
      result= self.ejecutar_query(query,"2")
      return result
    def select_notas(self,idUsuario):
      query="SELECT * FROM notas WHERE id_usuario= %i"%(idUsuario)
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      print("NOTAS====",data)
      return data
    def insert_nota(self, idUsuario, nota):

      query="INSERT INTO notas (id_usuario, nota)VALUES (%i,'%s')"%(idUsuario,nota)
      result=self.ejecutar_query(query,"2")

#insert de paciente   

    def insert_paciente(self, nombre, fecha_nacimiento, sexo, lugar_nacimiento, curp, tipo_sangre, pre_enfermedades, alergias, contacto, contacto_referencia, transitorio, direccion):
      query=('INSERT INTO pacientes (nombreCompleto, fechaNacimiento, sexo, lugarNacimiento, curp, grupoSanguineo, enfermedadesPree, alergias, contactoPaciente, contactoReferencias, idTipoPaciente, direccionPaciente) '
              f'VALUES ("{nombre}", "{fecha_nacimiento}","{sexo}","{lugar_nacimiento}","{curp}","{tipo_sangre}","{pre_enfermedades}","{alergias}","{contacto}","{contacto_referencia}","{transitorio}", "{direccion}")')
      self.ejecutar_query(query,"2")

    def select_pacientes(self):
      query="SELECT idPaciente, nombreCompleto, Sexo, floor(datediff (now(), fechaNacimiento)/365) from pacientes WHERE 1"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pacientes_info(self,id):
      query="SELECT idPaciente, nombreCompleto, sexo, grupoSanguineo, enfermedadesPree, alergias, contactoPaciente, floor(datediff (now(), fechaNacimiento)/365), fechaNacimiento from pacientes WHERE idPaciente = ('%s')"%(id)
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pacientes_internado(self,id):
      query="SELECT i.idHabitacion, i.fechaIngreso, i.fechaAlta, t.tipoInternado FROM internados as i, tipointernados as t WHERE i.idPaciente = ('%s') and i.idTipoInternado = t.idTipoInternado"%(id)
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pacientes_consulta(self,id):
      query="SELECT  u.nombreUsuario, fecha, hora, diagnostico FROM consultas as c, consultorios as con, usuarios as u WHERE c.idPaciente = ('%s') and con.idUsuario = u.idUsuario"%(id)
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pacientes_examen(self,id):
      query="SELECT fechaSolicitud, e.Nombre, resultados FROM historialexamenes as h, usuarios as u, examenes as e WHERE h.idPaciente = ('%s') and h.idExamen = e.idExamen and h.idUsuario = u.idUsuario and h.status = 2"%(id)
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def insert_doctor(self, nombre, contacto, especialidad):
      query=('INSERT INTO doctores (nombre, contacto, especialidad) '
              f'VALUES ("{nombre}", "{contacto}","{especialidad}")')
      self.ejecutar_query(query,"2")
    
    def select_nombre_pacientes(self):
      query="SELECT nombre FROM paciente"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data
    
    def select_examenes(self):
      query= "SELECT * from examenes"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def insert_examen(self,comentario,id_doctor,nombre_paciente,id_examen):
      
      try:
        id_paciente = self.get_id_paciente(nombre_paciente)
        
        if id_paciente:
          today = date.today()
          d1 = today.strftime("%Y-%m-%d")
          query=('INSERT INTO historialExamenes (fechaSolicitud, comentario, idUsuario, idPaciente, idExamen,status)'
              f'VALUES ("{d1}", "{comentario}","{id_doctor}","{id_paciente}","{id_examen}","0")')
          print("QUERY",query)
          self.ejecutar_query(query,"2")
          return True
        else:
          return False
      except:
        return False
      
    
    def get_id_paciente(self,nombre):
      try:
        query= f'Select idPaciente FROM pacientes WHERE nombreCompleto = "{nombre}"'
        cursor= self.ejecutar_query(query,"1")
        resultado = cursor.fetchone()
        id_usuario= str(resultado[0])
        return id_usuario
      except:
        return False



    def insert_consulta(self, id_consultorio, id, fecha, hora):
      query=('INSERT INTO consultas (idConsultorio, idPaciente, fecha, hora) '
              f'VALUES ("{id_consultorio}","{id}","{fecha}","{hora}")')
      print("AQui========",query)

      self.ejecutar_query(query,"2")


    def get_historial_examenes(self):
      try:
        query= ('Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario, p.nombreCompleto, '
                ' e.nombre, h.status FROM historialExamenes as h INNER JOIN usuarios as u INNER JOIN pacientes as p '
                ' INNER JOIN examenes as e WHERE h.idUsuario=u.idUsuario AND h.idPaciente = p.idPaciente '
                ' AND h.idExamen= e.idExamen')
        cursor= self.ejecutar_query(query,"1")
        examenes = cursor.fetchall()
        return examenes
      except:
        return False

    def select_examen(self,id):
      query= ("Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario, p.nombreCompleto," 
              "e.nombre, h.resultados FROM historialExamenes as h INNER JOIN usuarios as u INNER JOIN pacientes as p "
              f"INNER JOIN examenes as e WHERE h.idHistorialExamen = {id} AND h.idUsuario=u.idUsuario AND "
              "h.idPaciente = p.idPaciente AND h.idExamen= e.idExamen")
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def get_examenes_pendientes(self):
      try:
        query= ('Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario, p.nombreCompleto, '
                ' e.nombre, h.status FROM historialExamenes as h INNER JOIN usuarios as u INNER JOIN pacientes as p '
                ' INNER JOIN examenes as e WHERE h.idUsuario=u.idUsuario AND h.idPaciente = p.idPaciente '
                ' AND h.idExamen= e.idExamen')
        cursor= self.ejecutar_query(query,"1")
        examenes = cursor.fetchall()
        return examenes
      except:
        return False

    def get_historial_examenes(self):
      try:
        query= ('Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario, p.nombreCompleto, '
                ' e.nombre, h.status FROM historialExamenes as h INNER JOIN usuarios as u INNER JOIN pacientes as p '
                ' INNER JOIN examenes as e WHERE h.idUsuario=u.idUsuario AND h.idPaciente = p.idPaciente '
                ' AND h.idExamen= e.idExamen')
        cursor= self.ejecutar_query(query,"1")
        examenes = cursor.fetchall()
        return examenes
      except:
        return False

    def select_examen(self,id):
      query= ("Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario, p.nombreCompleto," 
              "e.nombre, h.resultados FROM historialExamenes as h INNER JOIN usuarios as u INNER JOIN pacientes as p "
              f"INNER JOIN examenes as e WHERE h.idHistorialExamen = {id} AND h.idUsuario=u.idUsuario AND "
              "h.idPaciente = p.idPaciente AND h.idExamen= e.idExamen")
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def get_examenes_pendientes(self):
      try:
        query= ('Select h.idHistorialExamen, h.fechaSolicitud, u.nombreUsuario, u.apellidoUsuario,'
                  'e.nombre FROM historialExamenes as h INNER JOIN usuarios as u '
                  'INNER JOIN examenes as e WHERE h.status = 0 AND  h.idUsuario=u.idUsuario AND h.idExamen= e.idExamen')
        cursor= self.ejecutar_query(query,"1")
        examenes = cursor.fetchall()
        return examenes
      except:
        return False

    def interna_paciente(self,id):
      query="Update pacientes set idTipoPaciente = 2 where idPaciente = %s"%(id)
      print(query)
      cursor= self.ejecutar_query(query,"2")
      data = cursor.fetchall()
      return data

    def select_pacientes_transitorios(self):
      query="SELECT idPaciente, nombreCompleto, Sexo, floor(datediff (now(), fechaNacimiento)/365) from pacientes WHERE idTipoPaciente = 1"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def select_pacientes_internados(self):
      query="SELECT idPaciente, nombreCompleto, Sexo, floor(datediff (now(), fechaNacimiento)/365) from pacientes WHERE idTipoPaciente = 2"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data