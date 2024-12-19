from flask import Blueprint, render_template, request, flash, redirect, url_for
from .scanner import verificar_portas, verificar_status
from .models import Tb_porta
from . import db


main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST'])
def check():

    portas_crud = Tb_porta.query.all()

    if request.method == "POST":
        url = request.form.get('url-input')

        # Chamar as funções de scanner
        status, response_time = verificar_status(url)

        # Extraindo o IP da URL
        host = url.replace("http://", "").replace("https://", "").split('/')[0]

        # Extraindo as portas através do CRUD
        portas_personalizadas = [porta.numero_porta for porta in portas_crud]

        # Verificar portas vulneraveis
        portas_abertas = verificar_portas(host, portas_personalizadas)

        # Lista todas as portas do banco de dados 
        portas_crud = Tb_porta.query.all()


        return render_template("index.html", status=status, response_time=response_time, url=url,
         portas_abertas=portas_abertas, portas_crud=portas_crud, portas_personalizadas=portas_personalizadas)
        
    return render_template("index.html", portas_crud=portas_crud)


@main.route('/adicionar', methods=['POST'])
def adicionar():
    numero_porta = request.form.get('numero-porta')
    descricao = request.form.get('descricao')
    id_porta = request.form.get('porta-id')


    if not numero_porta:
        flash('Número da porta é obrigatório!', 'error')
        return redirect(url_for('main.check'))

    try:
        if id_porta:  # Se um ID foi enviado, é uma edição
            porta_existente = Tb_porta.query.get(id_porta)
            if porta_existente:
                porta_existente.numero_porta = int(numero_porta)
                porta_existente.descricao = descricao
                db.session.commit()
                flash('Porta editada com sucesso!', 'success')
        else:  # Caso contrário, é uma nova adição
            nova_porta = Tb_porta(numero_porta=int(numero_porta), descricao=descricao)
            db.session.add(nova_porta)
            db.session.commit()
            flash('Porta adicionada com sucesso!', 'sucess')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro: {e}', 'error')
    
    return redirect(url_for('main.check'))



@main.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    # Atualiza as informações de uma porta já existente
    porta_existente = Tb_porta.query.get_or_404(id)
    novo_numero_porta = request.form.get('numero-porta')
    nova_descricao = request.form.get('descricao')

    if novo_numero:
        porta_existente.numero_porta = novo_numero_porta
        porta_existente.descricao = nova_descricao
        db.session.commit()
        flash('Porta editada com sucesso.', 'sucess')
    else:
        flash('Número da porta igual ou não existente!', 'error')

    return redirect(url_for('main.check'))



@main.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    porta_existente = Tb_porta.query.get_or_404(id)
    db.session.delete(porta_existente)
    db.session.commit()
    flash('Porta exluída!', 'error')

    return redirect(url_for('main.check'))




    
    




