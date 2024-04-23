from models.session import Session

def get_all_session():
    sessions = Session.read()
    return [sess.toJSON() for sess in sessions]

def get_session_with_id(id):
    return Session.read(id).toJSON()

def save_session(name, id=None):
    if id is not None:
        # get session with id
        session = Session.read(id)
        session.name = name
    else:
        session = Session(name=name)
    
    session.save()
    return session.toJSON()

def delete_session(id):
    session = Session.read(id)
    if session:
        session.delete()
        return session.toJSON()
    else:
        return {"message": "Session not found"}