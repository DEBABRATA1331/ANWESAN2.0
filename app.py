from flask import Flask, render_template, request, redirect, url_for, session, flash
import uuid
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ------------------ ROUTES ------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name'].strip()

        if not name:
            flash("Name is required!", "error")
            return redirect(url_for('login'))

        user_id = str(uuid.uuid4())[:8]
        session['name'] = name
        session['user_id'] = user_id

        return redirect(url_for('dashboard'))

    return render_template('login.html')
@app.route('/excom')
def excom():
    return render_template('excom.html')

@app.route('/dashboard')
def dashboard():
    if 'name' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', name=session['name'], user_id=session['user_id'])

@app.route('/certificate')
def certificate():
    if 'name' not in session:
        return redirect(url_for('login'))
    return render_template('certificate.html', name=session['name'])

# ------------------ MAIN ------------------

if __name__ == '__main__':
    app.run(debug=True)
