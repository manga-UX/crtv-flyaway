# 🛰️ CRTV Fly-Away Monitor v3.3

**Système de monitoring en temps réel pour transmission satellite** avec authentification d'agents, analyse IA et génération de rapports.

---

## 📋 Nouveautés v3.3

### ✨ Authentification des Agents
- **Matricule** : identifiant unique (ex. MAT001)
- **Mot de passe** : hashé en SHA-256, jamais stocké en clair
- **Lieu Production** : sélection parmi 8 antennes CRTV
- **Rôle** : Ingénieur Senior, Technicien, Opérateur

### 📊 Génération de Rapports Transmission
**Rapport Excel complet** contenant :
1. **Résumé Exécutif** : infos agent, KPIs, état global
2. **Données Détaillées** : toutes les mesures de la fenêtre temps réel
3. **Analyses Statistiques** : moyenne, écart-type, min/max par métrique
4. **Recommandations** : actions concrètes basées sur l'état système

Le rapport est téléchargeable directement depuis l'interface.

### 🔧 Améliorations Techniques
- Indépendant de l'horloge système (réf. temporelle = dernière donnée du fichier)
- Chemins portables (Windows, Linux, macOS, Streamlit Cloud)
- Upload fichier de secours si pas trouvé au chemin par défaut
- Logo facultatif (pas de plantage s'absent)

---

## 🚀 Déploiement Local

### 1. Cloner le dépôt
```bash
git clone https://github.com/VOTRE_USERNAME/crtv-flyaway.git
cd crtv-flyaway
```

### 2. Créer l'environnement virtual
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# OU
venv\Scripts\activate            # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Préparer les données
Créez un dossier `data/` et placez-y votre fichier Excel :
```
crtv-flyaway/
├── app.py
├── requirements.txt
├── agents.json
├── data/
│   └── flyaway_log_annuel_2025-1.xlsx
└── assets/
    └── logo-crtv.png (optionnel)
```

### 5. Exécuter l'app
```bash
streamlit run app.py
```

L'app s'ouvre à `http://localhost:8501`.

### Identifiants de démo
- **MAT001** / `demo123` (Ingénieur Senior — Yaoundé)
- **MAT002** / `demo123` (Technicien — Douala)
- **MAT003** / `demo123` (Opérateur — Buea)

---

## 📦 Déploiement sur Streamlit Cloud

### 1. Préparer le dépôt GitHub

```bash
git add .
git commit -m "CRTV Fly-Away v3.3 - Authentification + Rapports"
git push origin main
```

**Important** : N'envoyez **PAS** votre fichier Excel réel si les données sont confidentielles. L'app permet aux utilisateurs de déposer leurs propres fichiers via l'interface.

### 2. Configurer sur share.streamlit.io

1. Allez sur **[share.streamlit.io](https://share.streamlit.io)**
2. Connectez-vous avec GitHub
3. Cliquez **New app**
4. Sélectionnez :
   - **Repository** : `crtv-flyaway`
   - **Branch** : `main`
   - **Main file path** : `app.py`
5. Cliquez **Deploy**

### 3. Gérer les Secrets (Production)

Si vous utilisez une vraie base de données ou une API externe :

**Localement** : créez `.streamlit/secrets.toml`
```toml
[database]
host = "your-db-host"
user = "your-user"
password = "your-password"
```

**Sur Streamlit Cloud** : dans **Settings → Secrets**, collez le contenu en TOML.

Accédez via :
```python
db_host = st.secrets["database"]["host"]
```

---

## 🔐 Gestion des Agents

### Ajouter un Agent

Modifiez `agents.json` localement :
```json
{
  "MAT004": {
    "nom": "New Agent Name",
    "password_hash": "hash_du_password",
    "lieu": "Yaoundé — Centre Principal",
    "role": "Ingénieur"
  }
}
```

**Générer un hash SHA-256** :
```python
import hashlib
pwd = "your_password"
hash_pwd = hashlib.sha256(pwd.encode()).hexdigest()
print(hash_pwd)
```

Puis committez le fichier :
```bash
git add agents.json
git commit -m "Ajouter MAT004"
git push
```

### En Production (Base de Données)

Remplacez `charger_agents_db()` par une requête vers votre DB :
```python
def charger_agents_db():
    # Ex. avec PostgreSQL
    conn = psycopg2.connect(st.secrets["db_url"])
    cur = conn.cursor()
    cur.execute("SELECT matricule, nom, password_hash, lieu, role FROM agents")
    ...
```

---

## 📊 Générer un Rapport

1. **Connectez-vous** avec un matricule/password valide
2. Sélectionnez votre **Lieu Production**
3. Allez à l'onglet **"📋 Rapport Transmission"**
4. Cliquez **"✨ Générer Rapport Excel"**
5. Téléchargez le fichier

Le rapport porte le timestamp actuel : `Rapport_FlyAway_20250815_143022.xlsx`

---

## 🤖 Chat IA Assistant

Posez des questions naturelles :

- **"Comment est la latence ?"** → Analyse complète
- **"Expliquer les prédictions"** → Tendance des 15 prochaines minutes
- **"Impact pluie ?"** → Affaiblissement signal + stratégies
- **"Recommandations"** → Actions immédiate, court, moyen, long terme

---

## 🛠️ Architecture Technique

### Modules Principaux

| Module | Responsabilité |
|--------|----------------|
| `charger_donnees()` | Lecture Excel (chemin ou upload) |
| `ModeleAIOptimisee` | RandomForest pour prédictions latence |
| `ChatbotIAPrediction` | Réponses aux questions utilisateur |
| `generer_rapport_excel()` | Export multi-feuilles (résumé, données, analyses, recom) |
| `verifier_authentification()` | Hash SHA-256 + vérification credentials |

### Flux Données

```
Fichier Excel
    ↓
pd.read_excel() → Nettoyage (timestamp, tri)
    ↓
df_recent (fenêtre 1h du timestamp max)
    ↓
Dashboard KPIs + Graphique Plotly
    ↓
ChatBot IA + Prédictions + Rapport Excel
```

### Authentification

```
Utilisateur saisit MAT + Password
    ↓
SHA-256 du password
    ↓
Comparaison avec hash dans agents.json
    ↓
Stockage en session_state (Streamlit)
    ↓
Affichage dans sidebar + rapport
```

---

## 📁 Structure du Projet

```
crtv-flyaway/
├── app.py                           # Application Streamlit
├── requirements.txt                 # Dépendances Python
├── agents.json                      # Base agents (MAT001, MAT002, ...)
├── README.md                        # Cette doc
├── .gitignore                       # Fichiers à ignorer
├── data/
│   └── flyaway_log_annuel_2025-1.xlsx   # Données (à ajouter)
└── assets/
    └── logo-crtv.png                # Logo (optionnel)
```

---

## ❌ Troubleshooting

### "Fichier Excel introuvable"
**Cause** : le fichier n'est pas dans `data/`  
**Solution** : 
- Vérifiez le chemin exact (sensible à la casse)
- Ou utilisez l'uploader dans la barre latérale

### "Erreur de chargement — No sheet named 'Donnees_2025'"
**Cause** : le nom de la feuille ne correspond pas  
**Solution** : 
- Ouvrez l'Excel et vérifiez le nom exact des feuilles
- Modifiez dans la barre latérale (défaut : `Donnees_2025`)

### "Rapport ne se génère pas"
**Cause** : pandas/openpyxl manquant ou conflit import  
**Solution** : 
```bash
pip install --upgrade openpyxl pandas
streamlit run app.py
```

### "Chat IA ne répond pas"
**Cause** : modèle pas bien entraîné (< 50 lignes)  
**Solution** : ajoutez plus de données au fichier Excel

### "Logo n'apparaît pas"
**Cause** : fichier `assets/logo-crtv.png` absent  
**Solution** : c'est normal, l'app affiche une icône 🛰️ à la place

---

## 🔄 Mises à Jour

Après chaque modification locale :
```bash
git add .
git commit -m "Description du changement"
git push origin main
```

Streamlit Cloud redéploie **automatiquement** dans 1-2 minutes.

---

## 📞 Support

**Auteur** : Moussa Manga Asser  
**Contact** : +237 690 537 181 | assermoussa19@gmail.com  
**Version** : 3.3.0

---

## 📜 Licence

Propriété CRTV — Utilisation interne uniquement.
