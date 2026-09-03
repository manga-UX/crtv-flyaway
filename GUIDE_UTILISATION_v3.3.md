# 📖 Guide Complet — CRTV Fly-Away v3.3

## 🆕 Quoi de Neuf dans v3.3 ?

Trois grandes améliorations :

### 1️⃣ Authentification des Agents
**Avant** : n'importe qui pouvait accéder au dashboard  
**Maintenant** : chaque agent doit se connecter avec son matricule et mot de passe

**Avantages** :
- ✅ Traçabilité : qui a généré quel rapport
- ✅ Sécurité : accès restreint aux personnels autorisés
- ✅ Audit : historique des connexions (facilement extensible)

### 2️⃣ Identification du Lieu Production
**Avant** : le lieu n'était pas enregistré  
**Maintenant** : le lieu est sélectionné à la connexion et inclus dans les rapports

**Lieux disponibles** :
- Yaoundé — Centre Principal
- Douala — Antenne Côtière
- Buea — Station Montagne
- Bafoussam — Antenne Ouest
- Garoua — Antenne Nord
- Bertoua — Antenne Est
- Kribi — Station Côte
- Kumba — Antenne Anglophone
- Autre (à préciser)

### 3️⃣ Génération de Rapports Fonctionnelle
**Avant** : le bouton "Générer Rapports" ne faisait rien  
**Maintenant** : génère un rapport Excel complet avec 4 feuilles

**Contenu du rapport** :

#### 📄 Feuille 1 : Résumé
- Infos agent (nom, matricule, rôle, lieu)
- Date/heure du rapport
- KPIs clés (latence moy, qualité, C/N₀, température)
- État global du système

**Exemple** :
```
CRTV FLY-AWAY — RAPPORT DE FIN DE TRANSMISSION

Informations Transmission
Agent                    | Moussa Manga Asser
Matricule               | MAT001
Lieu Production         | Yaoundé — Centre Principal
Rôle                    | Ingénieur Senior

Statistiques Transmission
Latence Moyenne         | 685ms
Latence Min/Max         | 620 / 750ms
Qualité Signal Moyenne  | 92.5%
C/N₀ Moyen             | 11.3dBHz
Température HPA         | 48.2°C

Statut Transmission
État Global             | 🟢 NORMAL
Nombre Points Mesure    | 325
Période Fenêtre         | 1h
```

#### 📊 Feuille 2 : Données Détaillées
Toutes les lignes de la dernière heure, brutes, prêtes pour analyse externe.

#### 📈 Feuille 3 : Analyses
Statistiques calculées par métrique :
- **Latence** : Moyenne, Médiane, Écart-type, Min, Max
- **Qualité Signal** : Moyenne, Min, Max
- **Température HPA** : Moyenne, Min, Max

#### ⚡ Feuille 4 : Recommandations
Recommandations textuelles adaptées à l'état actuel :

**Si Latence > 800ms (CRITIQUE)** :
```
🔴 LATENCE CRITIQUE (> 800ms) — INTERVENTION IMMÉDIATE REQUISE

1. Vérifier pointage antenne (Azimut/Élévation)
2. Consulter météo locale (pluie, vent)
3. Augmenter FEC DVB-S2 si C/N₀ bas
4. Préparer basculement vers liaison alternative
```

**Si Latence > 720ms (ATTENTION)** :
```
🟡 LATENCE ÉLEVÉE (> 720ms) — À SURVEILLER

1. Optimiser paramètres DVB-S2
2. Ajuster buffer jitter encodeur
3. Surveiller température HPA
```

**Si Normal** :
```
🟢 SITUATION NORMALE

• Maintenir configuration actuelle
• Surveiller tendances horaires
```

+ alertes supplémentaires si température élevée ou pluie forte.

---

## 🔐 Authentification : Mode d'Emploi

### Écran de Connexion

À chaque lancement de l'app, vous voyez :

```
🛡️ Connexion Agent CRTV

Matricule    [MAT001              ]
Mot de passe [••••••              ]
Lieu Prod.   [Yaoundé ▼           ]

🔓 Se Connecter
```

### Étape 1 : Saisir le Matricule

Les matricules disponibles sont stockés dans `agents.json` :
```json
{
  "MAT001": { "nom": "Moussa Manga Asser", ... },
  "MAT002": { "nom": "Jean Dupont", ... },
  "MAT003": { "nom": "Marie Tagne", ... }
}
```

Tapez votre matricule (ex. `MAT001`).

### Étape 2 : Saisir le Mot de Passe

Le mot de passe est hashé en **SHA-256**. Jamais stocké en clair.

**Identifiants de démo** :
- Matricule : `MAT001`
- Mot de passe : `demo123`

> En production, changez ces mots de passe dans `agents.json`.

### Étape 3 : Choisir le Lieu Production

Sélectionnez votre lieu opérationnel dans la liste déroulante.

Exemple pour Douala :
```
Lieu Production : [Douala — Antenne Côtière ▼]
```

### Étape 4 : Se Connecter

Cliquez **🔓 Se Connecter**.

**Si succès** :
```
✅ Bienvenue Moussa Manga Asser !
(refresh automatique du dashboard)
```

**Si erreur** :
```
❌ Matricule introuvable
❌ Mot de passe incorrect
```

### Après Connexion

Dans la barre latérale, vous voyez votre profil :

```
👤 Agent Connecté
Moussa Manga Asser
Matricule : MAT001
Rôle : Ingénieur Senior
Lieu : Yaoundé — Centre Principal

🔓 Déconnexion
```

Cliquez **🔓 Déconnexion** pour revenir à l'écran de connexion.

---

## 📊 Générer un Rapport Transmission

### Accès

1. Connectez-vous (voir section Authentification)
2. Allez à l'onglet **"📋 Rapport Transmission"**

### Procédure

1. Lisez la description :
   > "Générez un rapport complet en Excel contenant : résumé, données détaillées, analyses statistiques et recommandations."

2. Cliquez le bouton **"✨ Générer Rapport Excel"**

3. Une barre de progression apparaît :
   ```
   ⏳ Génération du rapport...
   ```

4. Quand c'est fini :
   ```
   ✅ Rapport généré avec succès !
   
   📥 Télécharger Rapport Excel
   
   💾 Le rapport contient : résumé exécutif, données détaillées, 
      analyses et recommandations.
   ```

5. Cliquez **"📥 Télécharger Rapport Excel"** pour sauvegarder le fichier.

### Nom du Fichier

Le rapport est nommé avec un timestamp : `Rapport_FlyAway_YYYYMMDD_HHMMSS.xlsx`

Exemple : `Rapport_FlyAway_20250815_143022.xlsx`

Chaque rapport généré a un timestamp unique → impossible de les confondre.

### Utilisation du Rapport

Une fois téléchargé :

1. Ouvrez avec **Excel**, **LibreOffice Calc**, ou **Google Sheets**
2. Naviguez entre les 4 feuilles (onglets en bas)
3. Partagez avec votre direction, archived pour audit, etc.

**Cas d'usage** :
- 📋 Rapport de transmission fin de service
- 📧 Envoyer à la direction en cas d'incident
- 📦 Archiver pour compliance/audit
- 📊 Analyser tendances sur plusieurs jours

---

## 👥 Gestion des Agents (Administrateurs)

### Ajouter un Nouvel Agent

#### Localement (avant déploiement)

1. Ouvrez `agents.json`
2. Générez un hash SHA-256 du mot de passe :

```python
import hashlib
password = "nouveau_motdepasse_123"
hash_pwd = hashlib.sha256(password.encode()).hexdigest()
print(hash_pwd)
# Sortie : "a1b2c3d4..." (64 caractères)
```

3. Ajoutez l'agent :

```json
{
  "MAT001": { ... },
  "MAT004": {
    "nom": "Alice Martin",
    "password_hash": "a1b2c3d4...",
    "lieu": "Douala — Antenne Côtière",
    "role": "Technicien"
  }
}
```

4. Committez et poussez :

```bash
git add agents.json
git commit -m "Ajouter agent MAT004"
git push origin main
```

#### Sur Streamlit Cloud

L'app redéploie automatiquement (quelques minutes).

### Modifier un Agent

Même procédure : éditez `agents.json`, committez, poussez.

### Changer de Mot de Passe

1. Générez le nouveau hash :
```python
import hashlib
new_pwd = "nouveau123"
hashlib.sha256(new_pwd.encode()).hexdigest()
```

2. Mettez à jour `agents.json`
3. Committez et poussez

---

## 💾 Gestion des Données

### Fichier Excel Attendu

L'app lit un fichier `.xlsx` avec la structure suivante :

```
Feuille : "Donnees_2025"

Colonnes recommandées :
timestamp                  (format : 2025-01-15 14:30:45)
latence_totale_ms          (float)
cn0_dbhz                   (float)
esn0_db                    (float)
qualite_signal_pct         (float)
jitter_ms                  (float)
ber                        (float)
temperature_hpa_c          (float)
temperature_buc_c          (float)
attenuation_pluie_db       (float)
symbol_rate_msps           (float)
...autres colonnes...
```

### Où Placer le Fichier

**Localement** :
```
crtv-flyaway/
├── app.py
├── data/
│   └── flyaway_log_annuel_2025-1.xlsx
```

**Sur Streamlit Cloud** :
L'uploader dans la barre latérale permet de déposer un fichier directement, sans besoin qu'il soit dans le dépôt.

### Mettre à Jour les Données

1. **Localement** : remplacez le fichier dans `data/`
2. Committez et poussez :
   ```bash
   git add data/flyaway_log_annuel_2025-1.xlsx
   git commit -m "Mise à jour données"
   git push
   ```
3. Streamlit Cloud redéploie, charge les nouvelles données

**Ou** : utilisez l'uploader pour tester rapidement une nouvelle version

---

## 🎯 Cas d'Usage Typiques

### Cas 1 : Agent en terrain génère rapport quotidien

1. Se connecte le matin avec `MAT001` / `demo123`
2. Sélectionne son lieu (ex. "Douala")
3. Consulte le dashboard pendant la transmission (1h)
4. À la fin de transmission, va à "📋 Rapport Transmission"
5. Clique "✨ Générer Rapport Excel"
6. Télécharge `Rapport_FlyAway_20250815_084530.xlsx`
7. Envoie par email à sa direction
8. Se déconnecte

### Cas 2 : Supervision centralisée (Yaoundé)

1. Agent de supervision se connecte
2. Consulte les métriques en temps réel
3. Si latence > 720ms, clique "Recommandations" dans le chat IA
4. Suit les recommandations (augmenter FEC, vérifier pointage, etc.)
5. Génère un rapport pour archive
6. Contacts les agents en terrain si intervention immédiate requise

### Cas 3 : Audit/Conformité

1. Administrateur accède à Streamlit Cloud
2. Génère un rapport pour chaque jour de la semaine
3. Archive tous les rapports (4 feuilles chacun)
4. Exporte pour audit interne

---

## 🛠️ Configuration Avancée

### Modifier les Seuils Alerte

Éditez les constantes au début du fichier `app.py` :

```python
SEUIL_LATENCE_WARN = 720    # Avertissement (🟡)
SEUIL_LATENCE_CRIT = 800    # Critique (🔴)
FENETRE_RECENTE = timedelta(hours=1)  # Fenêtre temps réel
```

### Ajouter un Nouveau Lieu Production

Modifiez `LIEUX_DISPONIBLES` dans `app.py` :

```python
LIEUX_DISPONIBLES = [
    "Yaoundé — Centre Principal",
    "Douala — Antenne Côtière",
    "Buea — Station Montagne",
    "MA_NOUVELLE_STATION",  # ← Ajout
    "Autre (à préciser)"
]
```

### Changer le Nom/Logo de l'App

- **Titre** : `st.set_page_config(...page_title="CRTV Fly-Away v3.3...")`
- **Icône** : `st.set_page_config(...page_icon="🛰️")`
- **Logo image** : mettez votre PNG dans `assets/logo-crtv.png`

---

## ❓ FAQ

**Q : Puis-je utiliser une vraie base de données pour les agents ?**  
A : Oui. Remplacez `charger_agents_db()` par une requête SQL (PostgreSQL, MySQL, etc.). Consultez la section "Production" du code.

**Q : Comment sauvegarder les rapports générés ?**  
A : Ils sont téléchargés sur votre machine. Organisez-les dans un dossier "Rapports_2025" pour archivage.

**Q : Puis-je ajouter d'autres métriques au rapport ?**  
A : Oui. Modifiez `generer_rapport_excel()` pour ajouter des colonnes, calculs, etc.

**Q : Que se passe-t-il si le fichier Excel change de format ?**  
A : L'app affichera une erreur. Adaptez les noms de colonnes ou vérifiez la feuille active.

**Q : Comment faire un rapport PDF au lieu d'Excel ?**  
A : Installez `reportlab` et remplacez `openpyxl` par du PDF generation. Un peu de refactoring.

---

## 📞 Support

Besoin d'aide ? Consultez la section **Troubleshooting** du `README.md`.

**Auteur** : Moussa Manga Asser  
**Version** : 3.3.0  
**Date** : Août 2025
