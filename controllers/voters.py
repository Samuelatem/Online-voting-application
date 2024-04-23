from models.voters import Voters  # Corrected class name to follow PEP 8 conventions

def get_all_voters():
    # Renamed the parameter to avoid shadowing the import statement
    voters_list = Voters.read()  # Corrected method call to match the method name
    
    return [voters.toJSON() for voters in voters_list]

def get_voters_with_id(id):
    voter = Voters.read(id)  # Corrected method call to match the method name
    if voter:
        return voter.toJSON()  # Added check if voter is not None before calling toJSON
    else:
        return None  # Return None if voter with given ID is not found

def save_voters(name, id=None):
    if id is not None:
        voter = Voters.read(id)  # Corrected method call to match the method name
        if voter:
            voter.name = name
        else:
            return None  # Return None if voter with given ID is not found
    else:
        voter = Voters(name=name)  # Corrected class instantiation to match the class name
    
    voter.save()

    return voter.toJSON()

def delete_voters(id):
    voter = Voters.read(id)  # Corrected method call to match the method name
    if voter:
        voter.delete()
        return voter.toJSON()
    else:
        return None  # Return None if voter with given ID is not found