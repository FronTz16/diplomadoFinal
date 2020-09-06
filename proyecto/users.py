from flask_login import UserMixin
from proyecto import login_manager

class user(UserMixin):
	"""docstring for user"""
	def __init__(self,id, nombre, apellido, id_tipo, contraseña, correo):

		self.id = id
		self.nombre= nombre
		self.apellido=apellido
		self.correo=correo
		self.contraseña=contraseña
		self.id_tipo=id_tipo

		#print("PASSWORD:==> ",contraseña)