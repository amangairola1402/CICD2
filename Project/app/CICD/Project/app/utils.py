role_descriptions = {
    "Agent": "The entity that performs the action.",
    "Theme": "The entity that is moved or the topic of the action.",
    "Instrument": "The entity used to perform the action.",
    "Experienced": "The entity that experiences or perceives something.",
    "Location": "The place where the action occurs.",
    "Source": "The starting point of the action.",
    "Goal": "The endpoint of the action.",
    "Recipient": "The entity that receives something.",
    "Manner": "The way in which the action is performed."
}

def format_roles(sentence, roles):
    formatted_roles = []
    for role in roles:
        description = role_descriptions.get(role, "Description not available.")
        formatted_roles.append({"role": role, "description": description})
    
    return {"sentence": sentence, "roles": formatted_roles}