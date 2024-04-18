from models.session import session

def get_all_session():
    session = session.read()

    return [ session.toJSON() for session in session ]

def get_session_with_id(id):
    return session.read(id).toJSON()

def save_session(name, id=None):
    if id != None:
        # get session with id
        session = get_session_with_id(id)
        session.name = name

    else:
        session = session(name=name)
    
    session.save()

    return session.toJSON()

def delete_session(id):
    session = get_session_with_id(id)
    session.delete()

    return session.toJSON()
