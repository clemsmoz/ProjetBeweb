from flask import Flask, render_template, request, session, redirect, flash, jsonify
from controller.login import verifyLog
import controller.user
import controller.password_add
import controller.valide_token
import DAO.queries_eval
import controller.evaluation
import controller.select_menu
import json

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
        # utilisation de variables globales pour le role et la section
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_admin.html')
    elif controller.valide_token.has_valid_token() == 'formateur':
        role="formateur"
        section = controller.valide_token.verify_section()
        # utilisation de variables globales pour le role et la section
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_formateur.html')
    elif controller.valide_token.has_valid_token() == 'apprenant':
        role="apprenant"
        section = controller.valide_token.verify_section()
        pseudo = controller.apprenant.get_apprenant()
        # utilisation de variables globales pour le role et la section
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        app.jinja_env.globals['pseudo'] = pseudo
        return render_template('accueil_apprenant.html')
    elif controller.valide_token.has_valid_token() == 'salarie':
        role="salarie"
        section = controller.valide_token.verify_section()
        # utilisation de variables globales pour le role et la section
        app.jinja_env.globals['role'] = role
        app.jinja_env.globals['section'] = section
        return render_template('accueil_salarie.html')
    else:
        return render_template('login.html', message='veuillez vous connecter')

# route pour la deconnexion et suppression du token 
@app.route('/logout')
def logout():
    session.pop('token', None)
    flash('Vous êtes déconnecté !')
    return redirect('/') 

##########################  Page Creation Utilisateur  ##################################

# route pour l'affichage du menu de creation utilisateur
@app.route('/create')
def post():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation_user.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route lors de la creation d'un admin
@app.route('/creaAdmin', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        controller.user.insertAdmin()
        return render_template('accueil_admin.html', alerte='Admin créé !')

# route lors de la creation d'un formateur
@app.route('/creaFormateur', methods=['POST'])
def form2():
    if request.method == 'POST':
        controller.user.insertFormateur()
        return render_template('accueil_admin.html', alerte='Formateur créé !')

# route lors de la creation d'un apprenant
@app.route('/creaApprenant', methods=['POST'])
def form3():
    if request.method == 'POST':
        controller.user.insertApprenant()
        return render_template('accueil_admin.html', alerte='Apprenant créé !')

# route lors de la creation d'un salarie
@app.route('/creaSalarie', methods=['POST'])
def form4():
    if request.method == 'POST':
        controller.user.insertSalarie()
        return render_template('accueil_admin.html', alerte='Salarie créé !')

##############################  Page MAJ Password  ######################################

# route pour affichage du menu de l'update du password
@app.route('/updatePass')
def updatePass():
    return render_template('update_pass.html')

# route pour la maj du password
@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    if request.method == 'POST':
        message = controller.password_add.updateThisPassword(request.method)
        controller.password_add.updateThisPassword(request.method)
        flash(message)
        return redirect('/')

############################  Page Liste Formation  ####################################

# route pour afficher une formation selectionnée
@app.route('/selectBloc')
def selectbloc():
    result = controller.select_menu.select_bloc()
    if result :
        id = result
        return render_template('liste_formation.html', id_bloc=id)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return "ce titre n'existe pas"

############################  Page Creation Formation  ####################################

# route vers le menu de creation d'une formation
@app.route('/createFormation')
def post2():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        return render_template('creation_formation.html')
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour la creation d'une formation
@app.route('/createFormationOk', methods=['POST'])
def postOk():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        message = controller.create_formation.insertFormation()
        return render_template('creation_formation.html', message=message)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'
    
##############################  Page Selection  ######################################

# route vers le menu de selection
@app.route('/selection')
def selection():
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        formations = controller.select_menu.list_formations()
        return render_template('selection.html', formations=formations)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour recupération de la liste d'activités
@app.route('/activite/<int:id>', methods=['GET'])
def getActivites(id):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès
        result = controller.select_menu.get_activites(id)
        activites = [activite.json() for activite in result]
        return json.dumps({'activites': activites})
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour recupération de la liste de cp    
@app.route('/cp/<int:id>', methods=['GET'])
def getCp(id):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès
        result = controller.select_menu.get_cps(id)
        cps = [cp.json() for cp in result]
        return json.dumps({'cps': cps})
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour recupération de la liste de modules
@app.route('/module/<int:id>', methods=['GET'])
def getModule(id):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès
        result = controller.select_menu.get_modules(id)
        modules = [module.json() for module in result]
        return json.dumps({'modules': modules})
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour recupération de la liste d'items
@app.route('/item/<int:id>', methods=['GET'])
def getItem(id):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès
        result = controller.select_menu.get_items(id)
        items = [item.json() for item in result]
        return json.dumps({'items': items})
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

##############################  DELETE formation  ############################### 

# affichage du menu de suppression
@app.route('/DeleteForm/<string:title>', methods=['GET'])
def deleteBlock(title):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        objBloc = controller.select_menu.get_object_bloc(title)
        return render_template('suppression_bloc.html', objBloc=objBloc)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# affichage du menu de suppression
@app.route('/DeleteForm/<string:table>/<int:id>', methods=['GET'])
def deleteBlockinTable(id, table):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        objBloc = controller.select_menu.get_object_bloc_by_id(id, table)
        return render_template('suppression_bloc.html', objBloc=objBloc, table=table, id=id)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour la suppression et retour vers la page de selection 
@app.route('/DeleteBloc/<string:table>/<int:id>', methods=['POST'])
def delete_bloc(table, id):
    if controller.valide_token.has_valid_token() == 'administrateur':
        # L'utilisateur est authentifié, permettre l'accès à la page
        message = controller.select_menu.deletB(table, id)
        formations = controller.select_menu.list_formations()
        return render_template('selection.html', formations=formations, message=message)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

##############################  update formation  ############################### 

# affichage du menu de maj
@app.route('/updateFormations/<string:table>/<int:id>', methods=['GET'])
def get_update_formations(id, table):
    if controller.valide_token.has_valid_token() == 'administrateur':
        objBloc = controller.select_menu.get_object_bloc_by_id(id, table)
        if table != 'item':
            objList = controller.select_menu.get_list_obj(id, table)
        return render_template('modification_formation.html', objBloc=objBloc, objList= objList, table=table, id=id)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

# route pour Maj un obj et les obj associés
@app.route('/updateBloc/<string:table>/<int:id>', methods=['POST'])
def update_formations(id, table):
    if controller.valide_token.has_valid_token() == 'administrateur':
        message = controller.select_menu.update_obj(id, table)
        formations = controller.select_menu.list_formations()
        return render_template('selection.html', message=message, formations=formations)
    else:
        # L'utilisateur n'est pas authentifié, rediriger vers la page de connexion
        return 'Veuillez vous connecter pour accéder à cette page'

##############################  Page Evaluation  ######################################

# affichage de la liste d'evaluations
@app.route('/evaluations', methods=['GET'])
def list_all_evaluations():
    evaluations = controller.evaluation.list_all_evaluations()
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

@app.route('/detail_evaluations/<int:id_evaluation>', methods=['GET'])
def get_evaluation(id_evaluation):
    evaluation = controller.evaluation.get_evaluation(id_evaluation)    
    return render_template('detail_evaluation.html', evaluation=evaluation)

##############################  Profil apprenant  ######################################

@app.route('/profil/<string:pseudo>', methods=['GET'])
def get_apprenant(pseudo):
    apprenant = controller.apprenant.get_apprenant(pseudo)
    return render_template('profil_apprenant.html', apprenant=apprenant)

if __name__ == '__main__':
        app.static_folder = 'static'
        app.run(host='0.0.0.0', port=5000)