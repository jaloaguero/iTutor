from passlib.hash import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password

def verify_password(password, hashed_password):
    return bcrypt.verify(password, hashed_password)