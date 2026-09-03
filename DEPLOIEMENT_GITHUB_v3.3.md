# 🚀 Guide de Déploiement — GitHub + Streamlit Cloud v3.3

Ce guide vous accompagne **étape par étape** pour :
1. Initialiser un dépôt GitHub
2. Déployer sur Streamlit Community Cloud
3. Gérer les secrets et mises à jour

---

## 📋 Pré-requis

✅ Compte GitHub (gratuit : github.com)  
✅ Compte Streamlit Cloud (gratuit : share.streamlit.io)  
✅ Git installé (`git --version` pour vérifier)  
✅ Les fichiers locaux prêts :

```
crtv-flyaway/
├── app.py
├── requirements.txt
├── agents.json
├── README.md
├── GUIDE_UTILISATION_v3.3.md
├── .gitignore
├── data/
│   └── flyaway_log_annuel_2025-1.xlsx (OPTIONNEL)
└── assets/
    └── logo-crtv.png (OPTIONNEL)
```

---

## 1️⃣ Créer le Dépôt GitHub

### Étape 1.1 : Initialiser localement

Ouvrez un terminal et naviguez vers votre projet :

```bash
cd path/to/crtv-flyaway
git init
```

Vérifiez que Git reconnaît votre dossier :
```bash
ls -la | grep .git
# Ou sur Windows : dir | findstr .git
```

### Étape 1.2 : Configurer Git (première fois)

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@gmail.com"
```

(Les guillemets doivent entourer le nom.)

### Étape 1.3 : Ajouter les fichiers au staging

```bash
git add .
```

Vérifiez ce qui sera commité :
```bash
git status
```

**Output attendu** :
```
On branch master

Initial commit

Changes to be committed:
  new file:   app.py
  new file:   requirements.txt
  new file:   agents.json
  new file:   README.md
  ...
```

### Étape 1.4 : Premier commit

```bash
git commit -m "Initial commit - CRTV Fly-Away v3.3"
```

### Étape 1.5 : Renommer la branche (optionnel)

GitHub préfère `main` à `master` :

```bash
git branch -M main
```

---

## 2️⃣ Créer le Dépôt sur GitHub

### Étape 2.1 : Aller sur github.com

1. Allez sur **[github.com](https://github.com)**
2. Connectez-vous (ou créez un compte gratuit)
3. En haut à droite, cliquez le **➕ (Plus)**
4. Sélectionnez **New repository**

### Étape 2.2 : Remplir les informations

| Champ | Valeur |
|-------|--------|
| **Repository name** | `crtv-flyaway` |
| **Description** | `CRTV Fly-Away Monitor v3.3 - Authentification + Rapports` |
| **Visibility** | Public (ou Private si données confidentielles) |
| **Initialize with README** | ❌ Ne cochez PAS (vous en avez déjà un) |
| **Add .gitignore** | ❌ Ne cochez PAS (vous en avez déjà un) |
| **.gitignore template** | None |
| **Add a license** | None (optionnel) |

Cliquez **Create repository**.

### Étape 2.3 : Lier le dépôt local

GitHub affiche maintenant des instructions. Copiez les commandes pour un dépôt existant :

```bash
git remote add origin https://github.com/VOTRE_USERNAME/crtv-flyaway.git
git branch -M main
git push -u origin main
```

**Remplacez `VOTRE_USERNAME`** par votre login GitHub (ex. `moussa-asser`).

### Étape 2.4 : Pousser le code

Exécutez les 3 commandes ci-dessus dans votre terminal :

```bash
git remote add origin https://github.com/VOTRE_USERNAME/crtv-flyaway.git
```

✅ Ajoute la connexion GitHub

```bash
git branch -M main
```

✅ Renomme la branche en `main`

```bash
git push -u origin main
```

✅ Pousse votre code sur GitHub

**Vous pouvez être demandé de vous authentifier** (token GitHub). Consultez : https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

Une fois fait, visitez `https://github.com/VOTRE_USERNAME/crtv-flyaway` pour vérifier que le code est bien en ligne.

---

## 3️⃣ Déployer sur Streamlit Cloud

### Étape 3.1 : Aller sur Streamlit Cloud

1. Allez sur **[share.streamlit.io](https://share.streamlit.io)**
2. Connectez-vous avec GitHub (ou créez un compte gratuit)

### Étape 3.2 : Créer une nouvelle app

1. Cliquez le bouton bleu **"New app"** en haut à gauche
2. Remplissez le formulaire :

| Champ | Valeur |
|-------|--------|
| **GitHub repository** | VOTRE_USERNAME/crtv-flyaway |
| **Branch** | `main` |
| **Main file path** | `app.py` |

3. Cliquez **Deploy**

### Étape 3.3 : Attendre le déploiement

Streamlit compile et démarre l'app (1-3 minutes).

**Vous verrez** :
1. "Building..." (installation dépendances)
2. "Running..." (démarrage de l'app)
3. ✅ **"App is ready"** → lien vers votre app

**URL de votre app** : `https://crtv-flyaway.streamlit.app/` (ou autre slug auto-généré)

Cliquez le lien pour voir l'app en action ! 🎉

---

## 4️⃣ Mises à Jour (Git Workflow)

### Chaque fois que vous modifiez le code localement

#### 4.1 : Vérifier les changements

```bash
git status
```

**Output** :
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   app.py
  modified:   agents.json

Untracked files:
  new file:   config.yaml
```

#### 4.2 : Ajouter les changements

```bash
git add .
```

Ou ajouter seulement certains fichiers :
```bash
git add app.py agents.json
```

#### 4.3 : Créer un commit

```bash
git commit -m "Description brève du changement"
```

**Exemples de messages** :
- `git commit -m "Ajouter agent MAT004"`
- `git commit -m "Fixer bug génération rapport"`
- `git commit -m "Augmenter seuil alerte latence à 750ms"`

#### 4.4 : Pousser sur GitHub

```bash
git push origin main
```

Streamlit Cloud **détecte automatiquement** le changement et redéploie en 1-2 minutes.

---

## 5️⃣ Gérer les Secrets (Production)

### ⚠️ NE PAS Commiter les Secrets

Les secrets (clés API, credentials DB, mots de passe) ne doivent jamais être versionnés.

### Utilisation de `.streamlit/secrets.toml`

#### 5.1 : Créer le fichier local (DEV)

```
crtv-flyaway/
└── .streamlit/
    └── secrets.toml
```

**Contenu** (exemple) :
```toml
[database]
host = "localhost"
user = "admin"
password = "my_secret_password"

[api]
key = "sk_test_..."
```

#### 5.2 : Ignorer le fichier

Vérifiez que `.gitignore` contient :
```
.streamlit/secrets.toml
```

**Ne commitez JAMAIS `secrets.toml`**.

#### 5.3 : Accéder aux secrets dans le code

```python
db_password = st.secrets["database"]["password"]
api_key = st.secrets["api"]["key"]
```

#### 5.4 : Configuration sur Streamlit Cloud

1. Allez à votre app sur **share.streamlit.io**
2. Cliquez ⋯ (trois points) → **Settings**
3. Allez à l'onglet **Secrets**
4. Collez votre configuration TOML :

```toml
[database]
host = "prod-db.example.com"
user = "prod_user"
password = "prod_password_here"
```

5. Cliquez **Save**

L'app redéploie avec les nouveaux secrets.

---

## 6️⃣ Gestion des Données (Excel)

### Où Placer le Fichier ?

#### Option A : Dans le dépôt (public)

```
crtv-flyaway/
├── data/
│   └── flyaway_log_annuel_2025-1.xlsx
```

**Avantage** : simple, chargement automatique  
**Inconvénient** : le fichier est public, ne pas utiliser si données confidentielles

#### Option B : Uploader via l'interface

L'app possède un **file_uploader** dans la barre latérale.

**Avantage** : données jamais stockées sur GitHub  
**Inconvénient** : doit uploader à chaque session (sur Streamlit Cloud)

#### Option C : Cloud Storage (Advanced)

Stockez le fichier sur Google Drive, AWS S3, etc., et téléchargez-le à chaque démarrage.

```python
# Exemple (à intégrer dans charger_donnees)
from google.colab import auth
from googleapiclient.discovery import build

auth.authenticate_user()
drive = build('drive', 'v3')
files = drive.files().list().execute()
```

**⚠️ Nécessite configuration avancée**.

---

## 7️⃣ Troubleshooting Déploiement

### "App failed to load"

**Cause** : erreur Python  
**Solution** :
1. Vérifiez `requirements.txt` : toutes les imports sont-elles listées ?
2. Testez localement : `streamlit run app.py`
3. Consultez les logs Streamlit Cloud (icône 🔥 en haut à droite)

### "Module not found: openpyxl"

**Cause** : dépendance manquante  
**Solution** :
```bash
pip install openpyxl
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Ajouter openpyxl"
git push
```

### "FileNotFoundError: flyaway_log_annuel_2025-1.xlsx"

**Cause** : fichier Excel pas dans `data/`  
**Solution** :
1. Ajoutez le fichier via git :
   ```bash
   git add data/flyaway_log_annuel_2025-1.xlsx
   git commit -m "Ajouter données"
   git push
   ```
2. Ou utilisez l'uploader dans l'app

### L'app ne se redéploie pas après git push

**Cause** : Streamlit Cloud pas lié, ou délai  
**Solution** :
1. Vérifiez que vous avez pushé sur `main` (pas une autre branche)
2. Attendez 2-3 minutes
3. Actualisez la page (Ctrl+F5)
4. Consultez les logs (icon en haut à droite)

---

## 8️⃣ Workflow Recommandé

```
CODE LOCAL
    ↓
git add . && git commit -m "..." && git push
    ↓
GITHUB (votre dépôt)
    ↓
Streamlit Cloud détecte le changement
    ↓
Redéploiement automatique (1-2 min)
    ↓
APP EN LIGNE mise à jour
```

**Exemple pratique** :

```bash
# Vous fixez un bug localement
# Testez : streamlit run app.py

# Satisfait ? Committez
git add app.py
git commit -m "Fixer crash génération rapport"
git push origin main

# Attendez 2 minutes
# La version en ligne est à jour
```

---

## 9️⃣ Bonnes Pratiques

### ✅ À FAIRE

- ✅ Committez régulièrement (au moins après chaque feature)
- ✅ Utilisez des messages de commit **clairs** et **informatifs**
- ✅ Testez localement avant de pousser
- ✅ Archivez les rapports générés
- ✅ Mettez à jour `agents.json` via git pour que les changements soient appliqués

### ❌ À ÉVITER

- ❌ Ne committez PAS de `.streamlit/secrets.toml`
- ❌ Ne stockez PAS les fichiers Excel volumineux si données confidentielles
- ❌ Ne modifiez PAS `requirements.txt` manuellement (utilisez `pip freeze`)
- ❌ Ne poussez PAS sans tester localement
- ❌ Ne laissez PAS de mots de passe en dur dans le code

---

## 🔟 Rollback (Si Quelque Chose Casse)

### Voir l'historique

```bash
git log --oneline
```

**Output** :
```
a1b2c3d (HEAD -> main) Fixer rapport
e4f5g6h Ajouter agent MAT004
i7j8k9l Initial commit
```

### Revenir à une version précédente

```bash
git revert a1b2c3d
git push origin main
```

Streamlit Cloud redéploie la version précédente.

---

## 📞 Référence Rapide

| Tâche | Commande |
|-------|----------|
| Voir les changements | `git status` |
| Ajouter tous les fichiers | `git add .` |
| Créer un commit | `git commit -m "message"` |
| Pousser sur GitHub | `git push origin main` |
| Voir l'historique | `git log --oneline` |
| Faire un rollback | `git revert <commit_id>` |
| Cloner le dépôt | `git clone https://github.com/...` |

---

## 📚 Ressources

- **GitHub Docs** : https://docs.github.com
- **Streamlit Cloud Docs** : https://docs.streamlit.io/deploy/streamlit-community-cloud
- **Git Cheatsheet** : https://education.github.com/git-cheat-sheet-education.pdf

---

## ✅ Checklist Déploiement

- [ ] Fichiers locaux prêts (app.py, requirements.txt, etc.)
- [ ] `.gitignore` configuré
- [ ] Compte GitHub créé et connecté
- [ ] Dépôt GitHub créé (`crtv-flyaway`)
- [ ] Code pushé sur GitHub (`git push origin main`)
- [ ] Compte Streamlit Cloud créé
- [ ] App créée sur Streamlit Cloud
- [ ] App en ligne et fonctionnelle
- [ ] Identifiants de démo testés (MAT001 / demo123)
- [ ] Rapport généré et téléchargé
- [ ] Documentation lue (README.md, GUIDE_UTILISATION_v3.3.md)

---

**Besoin d'aide ?** Consultez la section **Troubleshooting** du README.md ou contactez l'auteur.

**Auteur** : Moussa Manga Asser  
**Version** : 3.3.0  
**Date** : Août 2025
