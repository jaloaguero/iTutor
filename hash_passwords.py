from passlib.hash import bcrypt

salt = b'$2b$12$X0CJdNij.qSMTBX39yr0VO'

def hash_password(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password

def verify_password(password_to_check, hashed_password):

    #if bcrypt.checkpw(password_to_check.encode('utf-8'), hashed_password):
    #    return True
    #else:
    return bcrypt.verify(password_to_check, hashed_password)