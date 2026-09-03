#!/usr/bin/env python3
"""
Script pour générer les hashes SHA-256 des mots de passe démo
À exécuter une fois pour initialiser agents.json avec les bons hashes
"""

import hashlib
import json

def hash_password(password: str) -> str:
    """Hash un mot de passe avec SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Générer les hashes pour "demo123"
password_demo = "demo123"
hash_demo = hash_password(password_demo)

print(f"Hash SHA-256 de '{password_demo}' : {hash_demo}")
print()

# Créer la base d'agents avec les bons hashes
agents_db = {
    "MAT001": {
        "nom": "Moussa Manga Asser",
        "password_hash": hash_demo,
        "lieu": "Yaoundé — Centre Principal",
        "role": "Ingénieur Senior"
    },
    "MAT002": {
        "nom": "Jean Dupont",
        "password_hash": hash_demo,
        "lieu": "Douala — Antenne Côtière",
        "role": "Technicien"
    },
    "MAT003": {
        "nom": "Marie Tagne",
        "password_hash": hash_demo,
        "lieu": "Buea — Station Montagne",
        "role": "Opérateur"
    }
}

# Sauvegarder dans agents.json
with open('agents.json', 'w', encoding='utf-8') as f:
    json.dump(agents_db, f, ensure_ascii=False, indent=2)

print("✅ agents.json mis à jour avec les bons hashes !")
print()
print("Contenu généré :")
print(json.dumps(agents_db, ensure_ascii=False, indent=2))
print()
print("Vous pouvez maintenant vous connecter avec :")
print("  Matricule : MAT001, MAT002, ou MAT003")
print(f"  Mot de passe : {password_demo}")
