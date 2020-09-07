from flask import Flask, render_template, url_for,flash, redirect, request
from proyecto.forms import registration_form, login_form, model_form, editar_pedido_form, tela_form,nota_form
from proyecto.conection import conexion, user
from proyecto import app, bcrypt
from proyecto.users import user
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
	
	return render_template('dashboard.html', title="Dashboard")

#LISTO
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
            return redirect(url_for('dashboard'))
        else:
            flash('Email o contraseña Incorrectos, Verifica', 'danger')
    return render_template('index.html', form=form,title="Login")

#LISTO
@app.route('/registro',methods=['GET','POST'])
#@login_required
def registro():
	print("REGISTRO")
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

# inicio de la base -----
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