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
    """Initialize the database with users table and migration support"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table with role support
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Simple migration: check if role column exists, if not add it
    try:
        cursor.execute("SELECT role FROM users LIMIT 1")
    except sqlite3.OperationalError:
        cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    
    conn.commit()
    conn.close()
    
    # Seed admin user
    seed_admin()
    print("Database initialized successfully!")

def seed_admin():
    """Create an initial admin user if not exists"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    admin_name = 'admin'
    admin_email = 'admin@plantai.com'
    admin_pass = hash_password('admin123')
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (admin_name,))
    if not cursor.fetchone():
        cursor.execute(
            'INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)',
            (admin_name, admin_email, admin_pass, 'admin')
        )
        conn.commit()
    conn.close()

def get_all_users():
    """Fetch all users for the admin dashboard"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, email, role, created_at FROM users WHERE role != "admin"')
    users = cursor.fetchall()
    conn.close()
    return [dict(u) for u in users]

def delete_user(user_id):
    """Delete a user by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return True

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
            'INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)',
            (username, email, hashed_password, 'user')
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
        'SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?',
        (username, username, hashed_password)
    )
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True, dict(user)
    return False, None
