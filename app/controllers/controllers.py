from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash, session
from functools import wraps
from app.models import db
from app.models.analise_solo import AnaliseSolo
from app.models.usuario import Usuario
from app.models.culturas import Cultura

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = Usuario.query.filter_by(email=email).first()
        if user and user.check_password(senha):
            session['user_id'] = user.cod_usuario
            return redirect(url_for('auth.home'))
        else:
            flash('Email ou senha inválidos')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if Usuario.query.filter_by(email=email).first() is None:
            user = Usuario(nome=nome, email=email)
            user.set_password(senha)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Email já registrado')
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
@login_required
def home():
    return render_template('home.html')

@auth_bp.route('/correcao')
@login_required
def correcao():
    culturas = Cultura.query.all()  # Recupera todas as culturas do banco de dados
    analises = AnaliseSolo.query.filter_by(cod_usuario=session['user_id']).all()  # Recupera todas as análises do usuário logado
    return render_template('correcao.html', culturas=culturas , analises=analises)


# Rota para editar e salvar análises de solo
@auth_bp.route('/analises', methods=['GET', 'POST'])
@login_required
def get_analises():
    if request.method == 'POST':
        
        #Verifica se é edição de análise
        if request.form['cod_analise']:
            # Obtendo a análise do banco de dados
            analise = AnaliseSolo.query.get(request.form['cod_analise'])
            # Atualizando os dados da análise
            analise.proprietario = request.form['proprietario']
            analise.vl_ph = request.form['ph']
            analise.vl_fosforo = request.form['fosforo']
            analise.vl_potassio = request.form['potassio']
            analise.vl_magnesio = request.form['magnesio']
            analise.vl_calcio = request.form['calcio']
            analise.vl_al = request.form['al']
            analise.vl_h_al = request.form['h_al']
            analise.vl_sb = request.form['sb']
            analise.vl_ctc = request.form['ctc']
            analise.vl_saturacao = request.form['saturacao']
            analise.vl_im = request.form['im']
            analise.vl_mo = request.form['mo']
            # Atualizando a análise no banco de dados
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Análise atualizada com sucesso', 'analise': {
                'cod_analise': analise.cod_analise,
                'data_cadastro': analise.data_cadastro.strftime('%Y-%m-%d'),
                'proprietario': analise.proprietario,
                'vl_ph': analise.vl_ph,
                'vl_fosforo': analise.vl_fosforo,
                'vl_potassio': analise.vl_potassio,
                'vl_magnesio': analise.vl_magnesio,
                'vl_calcio': analise.vl_calcio,
                'vl_h_al': analise.vl_h_al,
                'vl_sb': analise.vl_sb,
                'vl_ctc': analise.vl_ctc,
                'vl_saturacao': analise.vl_saturacao,
                'vl_im': analise.vl_im,
                'vl_mo': analise.vl_mo,
                'vl_al': analise.vl_al
            }}), 200  # 200 OK
            
        else:
            # Criação de uma nova análise a partir dos dados do formulário
            nova_analise = AnaliseSolo(
                cod_usuario= session['user_id'],  # Obtendo o ID do usuário da sessão
                proprietario=request.form['proprietario'],
                vl_ph=request.form['ph'],
                vl_fosforo=request.form['fosforo'],
                vl_potassio=request.form['potassio'],
                vl_magnesio=request.form['magnesio'],
                vl_calcio=request.form['calcio'],
                vl_h_al=request.form['h_al'],
                vl_sb=request.form['sb'],
                vl_ctc=request.form['ctc'],
                vl_saturacao=request.form['saturacao'],
                vl_im=request.form['im'],
                vl_mo=request.form['mo'],
                vl_al=request.form['al']
            )
            # Adicionando a nova análise ao banco de dados
            db.session.add(nova_analise)
            db.session.commit()

            # Retorna a análise salva em JSON
            return jsonify({'status': 'success', 'message': 'Análise salva com sucesso', 'analise': {
                'cod_analise': nova_analise.cod_analise,
                'data_cadastro': nova_analise.data_cadastro.strftime('%Y-%m-%d'),
                'proprietario': nova_analise.proprietario,
                'vl_ph': nova_analise.vl_ph,
                'vl_fosforo': nova_analise.vl_fosforo,
                'vl_potassio': nova_analise.vl_potassio,
                'vl_magnesio': nova_analise.vl_magnesio,
                'vl_calcio': nova_analise.vl_calcio,
                'vl_al': nova_analise.vl_al, # Adicionado o campo 'vl_al' na resposta JSON 23/06/2021
                'vl_h_al': nova_analise.vl_h_al,
                'vl_sb': nova_analise.vl_sb,
                'vl_ctc': nova_analise.vl_ctc,
                'vl_saturacao': nova_analise.vl_saturacao,
                'vl_im': nova_analise.vl_im,
                'vl_mo': nova_analise.vl_mo
            }}), 201  # 201 Created
    else:
        return render_template('analise.html')

# Rota para retornar análises de solo JSON
@auth_bp.route('/listar-analises', methods=['GET'])
def listar_analises():
    # Obtendo todas as análises do banco de dados
    analises = AnaliseSolo.query.filter_by(cod_usuario=session['user_id']).all()
    # Criando uma lista com os dados das análises
    analises_list = []
    for analise in analises:
        analises_list.append({
            'cod_analise': analise.cod_analise,
            'data_cadastro': analise.data_cadastro.strftime('%Y-%m-%d'),
            'proprietario': analise.proprietario,
            'vl_ph': analise.vl_ph,
            'vl_fosforo': analise.vl_fosforo,
            'vl_potassio': analise.vl_potassio,
            'vl_magnesio': analise.vl_magnesio,
            'vl_calcio': analise.vl_calcio,
            'vl_al': analise.vl_al, # Adicionado o campo 'vl_al' na resposta JSON 23/06/2021
            'vl_h_al': analise.vl_h_al,
            'vl_sb': analise.vl_sb,
            'vl_ctc': analise.vl_ctc,
            'vl_saturacao': analise.vl_saturacao,
            'vl_im': analise.vl_im,
            'vl_mo': analise.vl_mo
        })
    return jsonify({'status': 'success', 'message': 'Análises carregadas com sucesso', 'analises': analises_list}), 200  # 200 OK

# Rota para deletar análises de solo
@auth_bp.route('/delete-analise', methods=['POST'])
def delete_analise():
    #cria uma lista para armazenar os dados da análise a ser deletada
    analises_dict = {
        'cod_analise': request.form['cod_analise']
    }
    
    # Deletando a análise do banco de dados
    AnaliseSolo.query.filter_by(cod_analise=analises_dict['cod_analise']).delete()
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Análise deletada com sucesso', 'analise': analises_dict}), 200  # 200 OK


# Rotas para tratamento de culturas

#Rota para edição e cadastro de novas culturas
@auth_bp.route('/culturas', methods=['GET', 'POST'])
@login_required
def culturas():
    if request.method == 'POST':
        # Obtendo os dados do formulário        
        nome_cultura = request.form.get('nome_cultura')
        data_cadastro = request.form.get('data_cadastro')
        vl_saturacao_minima = request.form.get('vl_saturacao_minima')
        vl_saturacao_recomendada = request.form.get('vl_saturacao_recomendada')
        sg_estado = request.form.get('sg_estado')

        # Verifica se os campo nome_cultura está presente na requisição     
        if not nome_cultura:
            return jsonify({'status': 'error', 'message': 'Todos os campos obrigatórios devem ser preenchidos : nome cultura'}), 400  # 400 Bad Request
        
        # Verifica se os campo data_cadastro está presente na requisição
        if not data_cadastro:
            return jsonify({'status': 'error', 'message': 'Todos os campos obrigatórios devem ser preenchidos : data de cadastro'}), 400

        # Verifica se os campo vl_saturacao_minima está presente na requisição
        if not vl_saturacao_minima:
            return jsonify({'status': 'error', 'message': 'Todos os campos obrigatórios devem ser preenchidos : valor de saturação mínima'}), 400
        
        # Verifica se os campo vl_saturacao_recomendada está presente na requisição
        if not vl_saturacao_recomendada:
            return jsonify({'status': 'error', 'message': 'Todos os campos obrigatórios devem ser preenchidos : valor de saturação recomendada'}), 400
        
        # Verifica se os campo sg_estado está presente na requisição
        if not sg_estado:
            return jsonify({'status': 'error', 'message': 'Todos os campos obrigatórios devem ser preenchidos : sigla do estado'}), 400
        
        # Verifica se é edição de cultura atraves da verificação do campo cod_cultura não pode ser vazio
        if request.form['cod_cultura']:
            # Obtendo a cultura do banco de dados
            cultura = Cultura.query.get(request.form['cod_cultura'])
            
            if not cultura:
                return jsonify({'status': 'error', 'message': 'Cultura não encontrada'}), 404  # 404 Not Found
            
            # Atualizando os dados da cultura
            cultura.nome = nome_cultura
            cultura.data_cadastro = cultura.data_cadastro
            cultura.vl_saturacao_minima = vl_saturacao_minima
            cultura.vl_saturacao_recomendada = vl_saturacao_recomendada
            cultura.sg_estado = sg_estado
            
            # Atualizando a cultura no banco de dados
            db.session.commit()
            
            # Retorna a cultura salva em JSON
            return jsonify({'status': 'success', 'message': 'Cultura atualizada com sucesso', 'cultura': {
                'cod_cultura': cultura.cod_cultura,
                'nome': cultura.nome,
                'data_cadastro': cultura.data_cadastro.strftime('%Y-%m-%d'),
                'vl_saturacao_minima': cultura.vl_saturacao_minima,
                'vl_saturacao_recomendada': cultura.vl_saturacao_recomendada,
                'sg_estado': cultura.sg_estado
            }}), 200  # 200 OK

        else:
            # Criação de uma nova cultura a partir dos dados do formulário
            nova_cultura = Cultura(
                cod_usuario=session['user_id'],  # Obtendo o ID do usuário da sessão
                nome=nome_cultura,
                vl_saturacao_minima=vl_saturacao_minima,
                vl_saturacao_recomendada=vl_saturacao_recomendada,
                sg_estado=sg_estado
            )

            # Adicionando a nova cultura ao banco de dados
            db.session.add(nova_cultura)
            db.session.commit()

            # Retorna a cultura salva em JSON
            return jsonify({'status': 'success', 'message': 'Cultura salva com sucesso', 'cultura': {
                'cod_cultura': nova_cultura.cod_cultura,
                'nome': nova_cultura.nome,
                'data_cadastro': nova_cultura.data_cadastro.strftime('%Y-%m-%d'),
                'vl_saturacao_minima': nova_cultura.vl_saturacao_minima,
                'vl_saturacao_recomendada': nova_cultura.vl_saturacao_recomendada,
                'sg_estado': nova_cultura.sg_estado
            }}), 201  # 201 Created
    else:
        return render_template('cultura.html')


#Rotas para listar culturas
@auth_bp.route('/listar-culturas', methods=['GET'])
def listar_culturas():
    culturas = Cultura.query.all()
    culturas_list = []
    for cultura in culturas:
        culturas_list.append({
            'cod_cultura': cultura.cod_cultura,
            'nome': cultura.nome,
            'data_cadastro': cultura.data_cadastro.strftime('%Y-%m-%d'), # Formata a data para 'YYYY-MM-DD
            'vl_saturacao_minima': cultura.vl_saturacao_minima,
            'vl_saturacao_recomendada': cultura.vl_saturacao_recomendada,
            'sg_estado': cultura.sg_estado
        })
    return jsonify({'status': 'success', 'message': 'Culturas carregadas com sucesso', 'culturas': culturas_list}), 200  # 200 OK


# Rota para edição de senha de usuário
@auth_bp.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuario():
    user = Usuario.query.get(session['user_id'])
    if request.method == 'POST':
        if request.form['senha']:
            user.set_password(request.form['senha'])
        db.session.commit()
        return redirect(url_for('auth.home'))
    return render_template('usuario.html', user=user)



