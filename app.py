from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'portfolio.db'

# Function to initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

# Define routes
@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Save the data to the database
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Redirect to the home page after form submission

    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
