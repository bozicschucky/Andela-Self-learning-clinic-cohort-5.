
""" This module is the main flask  file that handles all the routes. """


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ This method handles the default 
    route which directs the user to 
    the login template."""
    #user = 'chucky'
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Routes to the register page"
     """
    return render_template('register.html')


@app.route('/logout')
def logout():
    """ Routes to the logout page
     """
    return render_template('logout.html')


@app.route('/dashboard')
def dashboard():
    """ Routes to the  home page 
    """
    #user = chucky
    #flash('welcome to the dashboard ')
    return render_template('index.html')


@app.route('/recipes')
def recipes():
    """Routes to the recipes page
    """
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)
