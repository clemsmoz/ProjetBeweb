from flask import Flask, render_template, request, session, redirect, flash, jsonify, url_for
from controller.login import verifyLog
import controller.user
import controller.password_add
import controller.valide_token
import DAO.queries_eval
import DAO.queries_activite
import DAO.queries_cp
import controller.evaluation
import controller.activite
import controller.cp


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
    evaluations = controller.evaluation.list_all_evaluations()
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/createEvaluations', methods=['GET', 'POST'])
def create_evaluation():
    if request.method == 'POST':
        titreEvaluation = request.form['titreEvaluation']
        dateEvaluation = request.form['dateEvaluation']
        coeffItem = request.form['coeffItem']
        coeffEval = request.form['coeffEval']
        noteEval = request.form['noteEval']
        noteItem = request.form['noteItem']
        controller.evaluation.create_evaluation()
        evaluations = controller.evaluation.get_all_evaluations()
        return redirect(url_for('evaluations'))
    else:
        return render_template('create_evaluations.html')

    
@app.route('/evaluations/<int:id_evaluation>', methods=['PUT'])
def update_evaluation(id_evaluation):
    titre = request.json.get('titre')
    date_evaluation = request.json.get('date_evaluation')
    DAO.queries_eval.update_evaluation(id_evaluation, titre, date_evaluation)
    evaluations =controller.evaluation.update_evaluation(id_evaluation, titreEvaluation, dateEvaluation)
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/evaluations/<int:id_evaluation>', methods=['DELETE'])
def delete_evaluation(id_evaluation):
    DAO.queries_eval.delete_evaluation(id_evaluation)
    evaluations = controller.evaluation.delete_evaluation(id_evaluation)
    return render_template('evaluations.html', evaluations=evaluations)

@app.route('/detail_evaluations/<int:id_evaluation>', methods=['GET'])
def get_evaluation(id_evaluation):
    evaluation = controller.evaluation.get_evaluation(id_evaluation)  
    return render_template('detail_evaluation.html', evaluation=evaluation)

@app.route('/competence', methods=['GET'])
def get_all_activite():
    activites = controller.activite.get_all_activite()
    return render_template('competence.html', activites=activites)

@app.route('/competence', methods=['GET'])
def get_all_cp():
    Cps = controller.cp.get_all_cp()
    return render_template('competence.html', Cps=Cps)






if __name__ == '__main__':
        app.static_folder = 'static'
        app.run(host='0.0.0.0', port=5000)