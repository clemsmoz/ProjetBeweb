from flask import Flask, render_template, request, session, redirect, flash
from controller.login import verifyLog
import controller.user
import controller.password_add
import controller.valide_token
import DAO.queries_eval


app = Flask(__name__)
app.secret_key = 'fondes2023'

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/verifyLogin', methods=['GET'])
def login():
    if request.method == 'GET':
        message = verifyLog()
        flash(message)
        verifyLog()
        return redirect('/accueil')

@app.route('/accueil')
def index():
    token = session.get('token')
    if controller.valide_token.has_valid_token() == 'administrateur':
        role="administrateur"
        section = controller.valide_token.verify_section()
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_admin.html')
    elif controller.valide_token.has_valid_token() == 'formateur':
        role="formateur"
        section = controller.valide_token.verify_section()
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_formateur.html')
    elif controller.valide_token.has_valid_token() == 'apprenant':
        role="apprenant"
        section = controller.valide_token.verify_section()
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_apprenant.html')
    elif controller.valide_token.has_valid_token() == 'salarie':
        role="salarie"
        section = controller.valide_token.verify_section()
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_salarie.html')
    else:
        return render_template('login.html', message='veuillez vous connecter')
    
@app.route('/logout')
def logout():
    session.pop('token', None)
    flash('Vous êtes déconnecté !')
    return redirect('/') 

@app.route('/create')
def post():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation_user.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'
    

@app.route('/creaAdmin', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        controller.user.insertAdmin()
        return render_template('accueil_admin.html', alerte='Admin créé !')

@app.route('/creaFormateur', methods=['POST'])
def form2():
    if request.method == 'POST':
        controller.user.insertFormateur()
        return render_template('accueil_admin.html', alerte='Formateur créé !')


@app.route('/creaApprenant', methods=['POST'])
def form3():
    if request.method == 'POST':
        controller.user.insertApprenant()
        return render_template('accueil_admin.html', alerte='Apprenant créé !')

@app.route('/creaSalarie', methods=['POST'])
def form4():
    if request.method == 'POST':
        controller.user.insertSalarie()
        return render_template('accueil_admin.html', alerte='Salarie créé !')


@app.route('/updatePass')
def updatePass():
    return render_template('update_pass.html')


@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    if request.method == 'POST':
        message = controller.password_add.updateThisPassword(request.method)
        controller.password_add.updateThisPassword(request.method)
        flash(message)
        return redirect('/')

@app.route('/createFormation')
def post2():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation_formation.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

@app.route('/selection')
def post3():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('selection.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'


@app.route('/evaluations', methods=['GET'])
def list_all_evaluations():
    evaluations = DAO.queries_eval.get_all_evaluations()
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/createEvaluations', methods=['POST'])
def create_evaluation():
    titre = request.json.get('titre')
    date_evaluation = request.json.get('date_evaluation')
    DAO.queries_eval.insert_evaluation(titre, date_evaluation)
    evaluations = DAO.queries_eval.get_all_evaluations()
    return render_template('create_evaluations.html', evaluations=evaluations), 201

@app.route('/evaluations/<int:id_evaluation>', methods=['PUT'])
def update_evaluation(id_evaluation):
    titre = request.json.get('titre')
    date_evaluation = request.json.get('date_evaluation')
    DAO.queries_eval.update_evaluation(id_evaluation, titre, date_evaluation)
    evaluations = DAO.queries_eval.get_all_evaluations()
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/evaluations/<int:id_evaluation>', methods=['DELETE'])
def delete_evaluation(id_evaluation):
    DAO.queries_eval.delete_evaluation(id_evaluation)
    evaluations = DAO.queries_eval.get_all_evaluations()
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/evaluations/<int:id_evaluation>', methods=['GET'])
def get_evaluation(id_evaluation):
    evaluation = DAO.queries_eval.get_evaluation_by_id(id_evaluation)
    if evaluation:
        return render_template('evaluations.html', evaluation=evaluation)
    else:
        return jsonify({'message': 'Evaluation not found'}), 404

@app.route('/createFormation')
def post2():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation_formation.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

@app.route('/selection')
def post3():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('selection.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

if __name__ == '__main__':
<<<<<<< HEAD
    app.static_folder = 'static'
    app.run(host='0.0.0.0', port=5000)

=======
        app.static_folder = 'static'
        app.run(host='0.0.0.0', port=5000)
>>>>>>> origin/test
