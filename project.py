import json

list_produits = [
    {"id": 1, "nom": "PC",  "prix": 4000, "quqntite": 25},
    {"id": 2, "nom": "telephone",  "prix": 3500,  "quantite": 35},
    {"id": 3, "nom": "clavier", "prix": 200.0,  "quantite": 20},
    {"id": 4, "nom": "souris", "prix": 95,  "quantite": 15},
    {"id": 5, "nom": "headphone", "prix": 90,  "quantite": 30},
]

def read():
    with open("product.json", "r") as f:
        return json.load(f)

def sauvegarder(list_produits):
    with open("product.json", "w") as f:
        json.dump(list_produits, f, indent=2)

def ajouter_produit(produits):
    id_prod = input("ID produit:")
    quantite = input("Quantité:")
    if not id_prod.isdigit():
        print("Entrée invalide");
    if not quantite.isdigit():
        print("Entrée invalide");

def menu():
    while True:
        print("\n1. list de produits")
        print("2. Ajouter au panier")
        print("3. Voir panier")
        print("4. Retirer du panier")
        print("5. Valider commande")
        print("6. Ajouter produit")
        print("7. Quitter")

        choix = input("Choix:")

        if choix == "2": 
            ajouter_produit()

        elif choix == "7": 
            print("goodbye! have a nice day!"); 
            break

        else:
            print("Choix invalide.")

     


 

