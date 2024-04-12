from models.voters import voters

def get_all_voters():
    voters = voters.read()

    return [ voters.toJSON() for voters in voters ]

def get_voters_with_id(id):
    return voters.read(id).toJSON()

def save_voters(name, id=None):
    if id != None:
        # get subject with id
        voters = get_voters_with_id(id)
        voters.name = name

    else:
        voters = voters(name=name)
    
    voters.save()

    return voters.toJSON()

def delete_voters(id):
    voters = get_voters_with_id(id)
    voters.delete()

    return voters.toJSON()
