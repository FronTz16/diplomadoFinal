from flask import Flask, render_template, url_for,flash, redirect, request
from flask_wtf import form
from proyecto.forms import registration_form, login_form, model_form, editar_pedido_form, tela_form,nota_form, nuevo_paciente_form, solicitar_examen_form
from proyecto.forms import nuevo_doctor_form, crear_consulta_form
from proyecto.conection import conexion, user
from proyecto import app, bcrypt
from proyecto.users import user
from flask_login import login_user, current_user, logout_user, login_required
from flask import jsonify

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
	
	return render_template('dashboard.html', title="Dashboard")

#LISTO

#LISTO
@app.route('/crear_modelo',methods=['GET','POST'])
@login_required
def crear_modelo():

	#conn=conexion()
	#telas_disponibles=conn.select('nombre_color',"tela","1","4")
	#form = model_form()
	#form.tela.choices=telas_disponibles
	
	if form.validate_on_submit():

		tipo_prenda=form.tipo_prenda.data
		peso_kg=form.peso_kg.data
		precio=form.precio.data
		id_tela=form.tela.data
		genero=form.genero.data
		nombre=form.nombre.data
		cantidad=form.cantidad.data
		conn=conexion()
		conn.insert_modelo(tipo_prenda,peso_kg,precio, id_tela, genero, nombre,cantidad)
		flash('Se ha creado correctamente el modelo', 'success')
		return redirect(url_for('modelos_ropa'))
	
	return render_template('crear_modelo.html', form=form,title="Crear Modelo")
#LISTO
@app.route('/usuarios')
#@login_required
def usuarios():
	conn=conexion()
	form=conn.select('*',"usuarios","1","2")
	return render_template('usuarios.html',form =form,title="Usuarios")
#LISTO
@app.route('/modelos_ropa')
@login_required
def modelos_ropa():
	conn=conexion()
	form=conn.select_modelos_ropa()
	return render_template('modelos_ropa.html',form =form,title="Modelos Ropa")

@app.route('/pedidos')
@login_required
def pedidos():

	conn=conexion()
	form=conn.select_pedidos()
	return render_template('pedidos.html',form=form, title="Pedidos")


@app.route('/telas')
@login_required
def telas():

	#conn=conexion()
	#form=conn.select_telas()
	return render_template('telas.html', title="Telas")

@app.route('/agregar_tela',methods=['GET','POST'])
@login_required
def agregar_tela():
	form=tela_form()

	if form.validate_on_submit():
		print("BANDERA AGREGAR")
		nombre_tela=form.color_tela.data
		peso=form.peso_kg.data
		conn=conexion()
		conn.insert_tela(nombre_tela,peso)
		flash('Se ha agrego la tela al inventario', 'success')
		return redirect(url_for('telas'))

	return render_template('crear_tela.html', form=form, title="Agregar Tela")

@app.route('/editar_tela/<id>',methods=['GET','POST'])
@login_required
def editar_tela(id):
	conn=conexion()
	info=conn.select("nombre_color","tela",id,"4")
	form=tela_form()
	print("INFO ", info)
	if form.validate_on_submit():
		color_tela=form.color_tela.data
		peso_kg=form.peso_kg.data
		conn=conexion()
		conn.update_telas(id,color_tela,peso_kg)
		flash('Se modifico la tela en el inventario', 'success')
		return redirect(url_for('telas'))
	
	return render_template('crear_tela.html',form=form,info=info, title="Editar Tela",tela=info[0][1])

@app.route('/editar_pedido/<id>',methods=['GET','POST'])
@login_required
def editar_pedido(id):
	conn=conexion()
	info=conn.select_1_pedido(id)

	form=editar_pedido_form()
	
	if form.validate_on_submit():
		
		estatus=form.estado_pedido.data
		print("BANDERA ESTATUS", estatus)
		if estatus is "5":
			
			if current_user.privilegios is "2":
				print("BANDERA PRIVILEGIOS",current_user.privilegios)
				conn.update_estatus_pedido(id,estatus)
				flash('Estatus Cambiado', 'success')
			else:
				flash('Solo un Administrador puede Cancelar un Pedido', 'danger')
			return redirect(url_for('pedidos'))
		else:
			conn.update_estatus_pedido(id,estatus)
			flash('Estatus Cambiado', 'success')
		return redirect(url_for('pedidos'))
	return render_template('editar_pedido.html',form=form,info=info,title="Editar Pedido")


@app.route("/logout")
def logout():
    logout_user()
    print("SESION CERRADA")
    return redirect(url_for('login'))


@app.route("/eliminar/<tabla>/<id>/<vista>")
@login_required
def eliminar(tabla,id,vista):

	conn=conexion()
	where="id= "+id
	conn=conn.delete(tabla,where)
	if conn:
		flash('Se ha eliminado correctamente', 'success')
	else:
		flash('No se elimino ningún registro', 'danger')
	return redirect(url_for(vista))

@app.route('/graficas')
#@login_required
def graficas():

	return render_template('graficas.html', title="Graficas")

# ========================================== Inicio Parte Medica ======================================================
@app.route('/login',methods=['GET','POST'])
def login():
    form=login_form()
    if form.validate_on_submit():
        conn=conexion()
        where="emailUsuario='"+form.email.data+"'"
		#Se crea el objeto usuario y se almacena en la variable usuario
        usuario=conn.select("*","usuarios",where,"1")
		#Se comprueba que las contraseñas coincidan
        if bcrypt.check_password_hash(usuario.contraseña,form.password.data):
            login_user(usuario)
            return redirect(url_for('base'))
        else:
            flash('Email o contraseña Incorrectos, Verifica', 'danger')
    return render_template('index.html', form=form,title="Login")

#LISTO
@app.route('/registro',methods=['GET','POST'])
#@login_required
def registro():

	form = registration_form()

	if form.validate_on_submit():

		nombres=form.nombres.data
		apellidos=form.apellidos.data
		email=form.email.data
		privilegios=form.privilegios.data
		h_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		conn=conexion()
		conn.insert_usuarios(nombres,apellidos,h_password, email, privilegios )
		flash('Se ha creado correctamente el usuario', 'success')
		return redirect(url_for('usuarios'))

	return render_template('crear_usuario.html', form=form, title="registro")

@app.route('/base')
#@login_required
def base():

	return render_template('base.html', title="Base")
# fin de la base --------

# ejemplo ------------------
@app.route('/nuevoExamen')
#@login_required
def nuevoExamen():

	return render_template('nuevo_examen.html', title="Graficas")
#fin del ejemplo ------------------------

# nuevo paciente ----------------------------------------------------------------
@app.route('/nuevo_paciente',methods=['GET','POST'])
#@login_required
def nuevoPaciente():
	form=nuevo_paciente_form()
	
	if form.validate_on_submit():
		print("AGREGAR")
		nombre=form.nombre.data
		fecha_nacimiento=form.fecha_nacimiento.data
		sexo=form.sexo.data
		lugar_nacimiento=form.lugar_nacimiento.data
		curp=form.curp.data
		tipo_sangre=form.tipo_sangre.data
		pre_enfermedades=form.pre_enfermedades.data
		alergias=form.alergias.data
		contacto=form.contacto.data
		contacto_referencia=form.contacto_referencia.data
		transitorio=form.transitorio.data
		direccion=form.direccion.data
		conn=conexion()
		conn.insert_paciente(nombre, fecha_nacimiento, sexo, lugar_nacimiento, curp, tipo_sangre, pre_enfermedades, alergias, contacto, contacto_referencia, transitorio, direccion)
		flash('Se agrego el paciente correctamente', 'success')
		return redirect(url_for('base'))


	return render_template('nuevo_paciente.html', form=form ,title="Nuevo Paciente")

# listado de pacientes----------------------------------------------------------
@app.route('/mis_pacientes')
#@login_required
def misPacientes():

	conn=conexion()
	form=conn.select_pacientes()
	return render_template('lista_pacientes.html', form=form, title="Mis Pacientes")

# historial paciente-----------------------------------------------------
@app.route('/historial_paciente/id/<id>')
#@login_required
def historial_paciente(id):

	conn=conexion()
	info = conn.select_pacientes_info(id)
	inter = conn.select_pacientes_internado(id)
	consu = conn.select_pacientes_consulta(id)
	exa = conn.select_pacientes_examen(id)
	
	return render_template('historial_paciente.html', info = info , inter = inter, consu = consu, exa = exa, title="historial")


# nuevo doctor ------------------
@app.route('/nuevo_doctor', methods=['GET', 'POST'])
# @login_required
def nuevoDoctor():
	form = nuevo_doctor_form()

	if form.validate_on_submit():
		nombre = form.nombre.data
		contacto = form.contacto.data
		especialidad = form.especialidad.data
		conn = conexion()
		conn.insert_doctor(nombre, contacto, especialidad)
		flash('Se agrego el docctor correctamente', 'success')
		return redirect(url_for('base'))

	return render_template('nuevo_doctor.html', form=form, title="Nuevo Doctor")

#================================= EXAMENES STUFF ================================
@app.route('/nuevo_examen', methods=['GET','POST'])
@login_required
def solicitar_examen():
	if current_user.id_tipo == 1:
		conn = conexion()
		examenes = conn.select_examenes()
		form = solicitar_examen_form()

		if form.is_submitted():
			
			comentario = form.comentarios_doctor.data
			id_doctor = current_user.id
			id_examen = int(request.form['id_examen'])
			nombre_paciente = form.nombre_paciente.data
			result = conn.insert_examen(comentario, id_doctor, nombre_paciente, id_examen)
			if result == True:
				flash('Se ha registrado el examen correctamente', 'success')
				return redirect(url_for('solicitar_examen'))
			else:
				flash('Ocurrio un error vuelva a intentar', 'danger')
				return redirect(url_for('solicitar_examen'))

		return render_template('nuevo_examen.html', exams=examenes, form=form, title="Nuevo Examen")
	else:
		flash('No tienes acceso a la url ingresada', 'danger')
		return redirect(url_for('base'))

# @app.route('/registar_nuevo_examen', methods=['GET', 'POST'])
# @login_required
# def crear_examen():

@app.route('/autocomplete_paciente_nombre',methods=['GET'])
@login_required
def autocomplete_paciente_nombre():
    conn = conexion()
    pacientes = conn.select_nombre_pacientes()
    resultList = []  
    for data_out in pacientes:  
        resultList.append(data_out[0])
    return jsonify(json_list=resultList)

@app.route('/historial_examenes',methods=['GET','POST'])
@login_required
def ver_historial_examenes():

	if current_user.id_tipo == 1 or current_user.id_tipo == 2:
		conn = conexion()
		historial = conn.get_historial_examenes()
		
		return render_template('historial_examenes.html', historial=historial, form=form, title="Historial Examenes")
	else:
		flash('No tienes acceso a la url ingresada', 'danger')
		return redirect(url_for('base'))

@app.route("/ver_examen/id/<id>")
@login_required
def ver_examen(id):

	if current_user.id_tipo == 1 or current_user.id_tipo == 2:
		conn=conexion()
		examen = conn.select_examen(id)
	else:
		flash('No tienes acceso a la url ingresada', 'danger')
		return redirect(url_for('base'))

	return render_template('ver_resultados_examen.html', examen = examen, title='Resultados')

@app.route('/examenes_pendientes',methods=['GET','POST'])
@login_required
def examenes_pendientes():	

	if current_user.id_tipo == 1: #cambiar el valor a 3 al terminar
		conn = conexion()
		examenes_pend = conn.get_examenes_pendientes()
		return render_template('examenes_pendientes.html', examenes=examenes_pend, title="Examenes Pendientes")
	else:
		flash('No tienes acceso a la url ingresada', 'danger')
		return redirect(url_for('base'))

@app.route('/nueva_consulta', methods=['GET', 'POST'])
@login_required
def nuevaConsulta():

	if current_user.id_tipo == 1 or current_user.id_tipo == 2:
		conn = conexion()
		form = crear_consulta_form()

		if form.is_submitted():

			id_paciente = form.id_paciente.data
			id_consultorio = form.id_consultorio.data
			fecha = form.fecha.data
			hora = form.hora.data
			result = conn.insert_consulta(id_paciente, id_consultorio, fecha, hora)
			print("Bandera")
			if result == True:
				flash('Se ha registrado la consulta correctamente', 'success')
				return redirect(url_for('base'))
			else:
				flash('Ocurrio un error vuelva a intentar', 'danger')
				return redirect(url_for('base'))

		return render_template('nueva_consulta.html', form=form, title="Nuevo Examen")
	else:
		flash('No tienes acceso a la url ingresada', 'danger')
		return redirect(url_for('base'))