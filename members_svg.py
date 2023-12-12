def generate_svg_with_members_count(members_count):
    svg_content = f'''
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="25">
        <rect width="150" height="25" style="fill: #555" />
        <text x="10" y="18" font-family="Arial" font-size="12" fill="white">
            Nombre de membres : {members_count}
        </text>
    </svg>
    '''
    
    with open('members_badge.svg', 'w') as file:
        file.write(svg_content)

# Utilisation de la fonction pour générer le badge SVG avec le nombre de membres
generate_svg_with_members_count(members_count)
