import json
import requests
import folium


# utilisation de l'API : https://geo.api.gouv.fr/adresse


# pip install requests
# pip install folium
# pip install json

def coordonnee(adresse,codepostal):
    """
    adresse = adresse sous forme de chaine de caractère
    codepostal = code de la ville
    return = [coordonnéeX,coordonnéeY]
    """
    url = 'https://api-adresse.data.gouv.fr/search/?q={0}+{1}&limit=1'.format(adresse.replace(' ','+'),codepostal)

    reponse = requests.get(url)
    data = json.loads(reponse.text)

    return [data['features'][0]['geometry']['coordinates'][1],data['features'][0]['geometry']['coordinates'][0]]

def carte(ville,codepostal,coordonneeListe):
    """
    ville = nom de la ville sous forme de chaine de caractère
    codepostal = code a 5 chiffres
    coordonneeListe = liste de coordonnée géographique
    RETURN = une carte de la ville avec les différents points
    """
    c = folium.Map(location=coordonnee(ville,codepostal),zoom_start=15)
    for e in coordonneeListe:
        folium.Marker(e).add_to(c)
    #c.save('carte.html')
    return c._repr_html_()


#carte("Paris 6",75006,[coordonnee("3 rue saint sulpice",75006),coordonnee("12 rue saint sulpice",75006)])