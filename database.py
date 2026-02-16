import sqlite3
import hashlib
from datetime import datetime

DATABASE_NAME = 'plant_disease.db'

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with users table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    """Register a new user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        hashed_password = hash_password(password)
        cursor.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, hashed_password)
        )
        conn.commit()
        conn.close()
        return True, "Registration successful!"
    except sqlite3.IntegrityError as e:
        conn.close()
        if 'username' in str(e):
            return False, "Username already exists!"
        elif 'email' in str(e):
            return False, "Email already exists!"
        return False, "Registration failed!"

def validate_login(username, password):
    """Validate user login credentials"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    cursor.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, hashed_password)
    )
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True, dict(user)
    return False, None

def get_user_by_email(email, password):
    """Get user by email and password"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    cursor.execute(
        'SELECT * FROM users WHERE email = ? AND password = ?',
        (email, hashed_password)
    )
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True, dict(user)
    return False, None
