import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create the portfolio_projects table
cursor.execute('''CREATE TABLE IF NOT EXISTS portfolio_projects (
                    id INTEGER PRIMARY KEY,
                    project_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    additional_details TEXT
                )''')

# Create the education_details table
cursor.execute('''CREATE TABLE IF NOT EXISTS education_details (
                    id INTEGER PRIMARY KEY,
                    university TEXT NOT NULL,
                    degree TEXT NOT NULL,
                    duration TEXT NOT NULL
                )''')

# Create the contact_submissions table
cursor.execute('''CREATE TABLE IF NOT EXISTS contact_submissions (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL
                )''')

# Commit changes and close the connection
conn.commit()
conn.close()
