from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField, SelectField,IntegerField, DecimalField,FileField, DateField,TextAreaField
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

# nuevos forms 

class nuevo_paciente_form(FlaskForm):
	nombre = StringField('Nombre completo',
						validators=[DataRequired(),Length(min=10, max=50)])

	fecha_nacimiento = DateField('Fecha de nacimiento',
						validators=[DataRequired('Seleciona una fecha')])

	sexo = SelectField('Genero',
		                    choices=[
										('Hombre','Hombre'),
										('Mujer','Mujer')])

	lugar_nacimiento = SelectField('Lugar de nacimiento',
		                                choices=[
										            ('CDMX','CDMX'),
										            ('Qro','Qro')])
	
	curp = StringField('Curp',
	                    validators=[DataRequired(),Length(min=1, max=18)])
	
	tipo_sangre = SelectField('Tipo de sangre',
	                            choices=[
                                            ('A+','A positivo'),
											('A-','A negativo'),
											('B+','B positivo'),
											('B-','B negativo'),
											('O+','O positivo'),
											('O-','O negativo'),
											('AB+','AB positivo'),
											('AB-','AB negativo')])
										
	pre_enfermedades = StringField('Preexistenias',
	                                validators=[DataRequired(),Length(min=1, max=50)])
							
	direccion = StringField('Dirección',
							validators=[DataRequired(),Length(min=1, max=120)])
	
	alergias = StringField('Alergias',
							validators=[DataRequired(),Length(min=1, max=20)])
						
	contacto = StringField('Teléfono',
	                        validators=[DataRequired(),Length(min=1, max=10)])

	contacto_referencia = StringField('Contacto de referencia',
	                    				validators=[DataRequired(),Length(min=1, max=10)])

	transitorio = SelectField('Status',
		                                choices=[
										            ('1','Transitorio'),
													('2','Internado')])
    
	submit= SubmitField('GUARDAR PACIENTE')


class nuevo_doctor_form(FlaskForm):
	nombre = StringField('Nombre completo',
						 validators=[DataRequired(), Length(min=10, max=50)])

	contacto = StringField('Teléfono',
						   validators=[DataRequired(), Length(min=1, max=10)])

	especialidad = StringField('Especialidad',
									  validators=[DataRequired(), Length(min=1, max=50)])


	submit = SubmitField('GUARDAR DOCTOR')


class solicitar_examen_form(FlaskForm):
	nombre_paciente = StringField('Nombre Paciente',
								  validators=[DataRequired(), Length(min=10, max=50)], id="nombre_paciente")

	comentarios_doctor = TextAreaField('Comentarios')

	submit = SubmitField('Solicitar Examen')


class crear_consulta_form(FlaskForm):

	id_consultorio = SelectField('Consultorio',
		                                choices=[
										            ('1','Consultorio mario')])
	fecha = DateField('Fecha')
	hora = StringField('Hora')
	submit = SubmitField('Crear consulta')


class resolver_examen_form(FlaskForm):
	resolucion = StringField('Resultados')
	submit = SubmitField()

class asignar_habitaciones(FlaskForm):

	doctor = StringField('Id doctor')
	submit = SubmitField()
