from passlib.hash import pbkdf2_sha256 as hasher


DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": hasher.hash("adminpw"),
    "normaluser": hasher.hash("normalpw"),
}

ADMIN_USERS = ["admin"]