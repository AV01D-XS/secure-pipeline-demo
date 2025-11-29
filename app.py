import os
import sqlite3

# --- VULNERABILITY 1: HARDCODED SECRET ---
# TruffleHog should scream when it sees this.
# NEVER do this in real life.
AWS_ACCESS_KEY_ID = "AKIA1234567890FAKEKEY"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user_data(username):
    # Connect to a dummy database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # --- VULNERABILITY 2: SQL INJECTION ---
    # Bandit and other SAST tools will flag this immediately.
    # The user input is concatenated directly into the query string.
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    print(f"Executing query: {query}")
    
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def main():
    print("Starting the Vulnerable App...")
    user = input("Enter username: ")
    get_user_data(user)

if __name__ == "__main__":
    main()
