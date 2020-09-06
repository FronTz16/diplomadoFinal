from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField, SelectField,IntegerField, DecimalField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registration_form(FlaskForm):
	nombres = StringField('Nombres',
						validators=[DataRequired(),Length(min=2, max=20)])

	apellidos = StringField('Apellidos',
							validators=[DataRequired(),Length(min=2, max=30)])

	email = StringField('Email',validators=[DataRequired(),Email()])

	privilegios =SelectField('Tipo Usuario',
							choices=[
								('1','Doctor'),
								('2','Enfermero'),
								('3','Laborista'),
								('4','Administrador')
								],default=1)

	password = PasswordField('Contraseña',
							validators=[DataRequired(),Length(min=5, max=20)])

	confirm_password = PasswordField('Confirmar contraseña',
									validators=[DataRequired(),
												Length(min=5, max=20),
												EqualTo('password')])

	submit= SubmitField('Registrar')


class login_form(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])

	password = PasswordField('Contraseña',validators=[DataRequired()])
	remember=BooleanField('remember_me')
	submit= SubmitField('Ingresar')


class model_form(FlaskForm):
	tipo_prenda = StringField('Tipo de Prenda',
						validators=[DataRequired(),Length(min=2)])

	peso_kg = DecimalField('Peso Kg',
							validators=[DataRequired()])

	precio =DecimalField('Precio',
							validators=[DataRequired()])

	tela=SelectField('Tela',coerce=int,default=1)

	genero = SelectField('Genero',
							choices=[
								('Mujer','Mujer'),
								('Hombre','Hombre'),
								('Niño','Niño'),
								('Niña','Niña')
								],default=1)

	nombre = StringField('Nombre',
						validators=[DataRequired(),Length(min=2)])

	cantidad = IntegerField('Piezas')

	picture = StringField('Cargar Imagen')

	submit= SubmitField('Registrar')


class editar_pedido_form(FlaskForm):

	estado_pedido=SelectField(choices=[
										('0','Pendiente'),
										('1','Cortando Tela'),
										('2','Armando Prenda'),
										('3','Ultimos Detalles'),
										('4','Enviado'),
										('5','Cancelado')])
	submit= SubmitField('Actualizar Estatus')

class tela_form(FlaskForm):
	color_tela = StringField('Nombre y Color',
						validators=[DataRequired(),Length(min=2)])

	peso_kg = DecimalField('Peso Kg',
							validators=[DataRequired()])

	submit= SubmitField('Agregar')

class nota_form(FlaskForm):
	nota = StringField('Nota',
						validators=[DataRequired(),Length(min=2, max=100)])
	submit= SubmitField('Guardar')