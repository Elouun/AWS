# AWS
Chalice
il faut avoir httpie (pip install httpie)
pour lancer en local : chalice local
lancer sur internet : chalice deploy
ensuite chalice url pour avoir l'url a remplacer pour les requetes

requete utilisable par le serveur : 

requete de selection de tout les objets:
http localhost:8000/todos

requete d'insertion :
echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos

requete de selection par id :
http localhost:8000/todos/XXXXXXXXXXXXXX (les x par l'uid trouvé avec l'affichage, il est généré aléatoirement)

suupression :
http DELETE localhost:8000/todos/XXXXXXXXXXXXX
