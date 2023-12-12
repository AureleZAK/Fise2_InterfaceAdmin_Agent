import requests

def get_project_members(project_id, private_token):
    url = f"https://gitlab.com/api/v4/projects/{project_id}"
    headers = {"PRIVATE-TOKEN": private_token}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        project_details = response.json()
        return project_details['statistics']['members_count']
    else:
        return None

# Utilisation de la fonction pour récupérer le nombre de membres d'un projet spécifique
project_id = https://devops.telecomste.fr/printerfaceadmin/2023-24/group4/agent
private_token = glpat-s6ra7F8y1k_ony-phY8y

members_count = get_project_members(project_id, private_token)
print(f"Nombre de membres : {members_count}")
