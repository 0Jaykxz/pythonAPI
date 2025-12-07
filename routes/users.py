from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from database.models.user import lojas

user_route = Blueprint('user', __name__)

@user_route.route('/')
def listar():
    pick = lojas.select()

    return render_template('label.html', markets = pick)

@user_route.route('/form')
def form():
    return render_template('form.html')

@user_route.route('/new', methods=['POST'])
def inserir():
    dados = request.get_json()

    lojas.create(
        name=dados['nome'],
        email=dados['email']
    )

    return jsonify({
        'mensagem': None,
        'redirect': url_for('user.listar')
    })

@user_route.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    u = lojas.get(lojas.id == id)
    u.delete_instance()

    return {'deleted': 'ok'}

@user_route.route('/edit/<int:id>')
def form_edit(id):
    edit = None
    cliente = lojas.select()
    for c in cliente:
        if c.id == id:
            edit = c

    return render_template('form.html', user = edit)

@user_route.route('/update/<int:id>', methods=['PUT'])
def update(id):
    dados = request.get_json()

    lojas.update(
        name=dados['nome'],
        email=dados['email']
    ).where(lojas.id == id).execute()
    return jsonify({
        'mensagem': None,
        'redirect': url_for('user.listar')
    })