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
      self.db="iDoctorv2"
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
      query=('INSERT INTO usuarios (nombreUsuario, apellidoUsuario, emailUsuario, password, id_tipo) '
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

    def insert_paciente(self, nombre, fecha_nacimiento, sexo, lugar_nacimiento, curp, tipo_sangre, pre_enfermedades, alergias, contacto, contacto_referencia, transitorio):
      query=('INSERT INTO paciente (nombre, fechaNacimiento, sexo, lugarNacimiento, curp, grupoSanguineo, enfermedadesPre, alergias, contacto, contactoReferencia, transitorio) '
              f'VALUES ("{nombre}", "{fecha_nacimiento}","{sexo}","{lugar_nacimiento}","{curp}","{tipo_sangre}","{pre_enfermedades}","{alergias}","{contacto}","{contacto_referencia}","{transitorio}")')
      self.ejecutar_query(query,"2")

    def select_pacientes(self):
      query="SELECT nombre, sexo, floor(datediff (now(), fechaNacimiento)/365) from paciente WHERE 1"
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
      query= "SELECT * from examen"
      cursor= self.ejecutar_query(query,"1")
      data = cursor.fetchall()
      return data

    def insert_examen(self,comentario,id_doctor,nombre_paciente,id_examen):
      
      try:
        id_paciente = self.get_id_paciente(nombre_paciente)
        
        if id_paciente:
          today = date.today()
          d1 = today.strftime("%Y-%m-%d")
          query=('INSERT INTO historial (fecha, comentario, idDoctor, idPaciente, idExamen)'
              f'VALUES ("{d1}", "{comentario}","{id_doctor}","{id_paciente}","{id_examen}")')
          self.ejecutar_query(query,"2")
          return True
        else:
          return False
      except:
        return False
      
    
    def get_id_paciente(self,nombre):
      try:
        query= f'Select idPaciente FROM paciente WHERE nombre = "{nombre}"'
        cursor= self.ejecutar_query(query,"1")
        resultado = cursor.fetchone()
        id_usuario= str(resultado[0])
        return id_usuario
      except:
        return False
    
    def get_historial_examenes(self):
      try:
        query= f'Select * h.idHistorial,h.fecha, d.idDoctor, p.idPaciente, e.idExamen FROM historial as h INNER JOIN doctores as d INNER JOIN pacientes as p INNER JOIN examen as e'
        cursor= self.ejecutar_query(query,"1")#from pedidos as p inner join prenda as pr INNER'
        resultado = cursor.fetchone()
        id_usuario= str(resultado[0])
        return id_usuario
      except:
        return False