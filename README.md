## Objectif du projet

Apprendre à construire une API REST complète avec architecture modulaire via routers, authentification JWT, gestion de base de données avec SQLAlchemy, validation des données avec Pydantic et sécurisation des mots de passe avec bcrypt.

# FastAPI Blog API - Authentication and CRUD

## Description

Ce projet est une API REST développée avec FastAPI permettant de gérer des utilisateurs et des blogs avec un système d’authentification basé sur JWT.

## Stack technique

FastAPI  
SQLAlchemy  
SQLite  
Pydantic  
bcrypt  
JSON Web Token (JWT)

## Fonctionnalités

### Utilisateurs
- Création d’utilisateurs
- Authentification avec email et mot de passe
- Hashage sécurisé des mots de passe avec bcrypt
- Relation entre utilisateurs et blogs

### Blogs
- Création de blogs
- Lecture des blogs
- Mise à jour des blogs
- Suppression des blogs

### Authentification
- Login utilisateur
- Génération de token JWT
- Protection des routes avec Bearer Token

## Structure du projet

## Project structure

Le projet contient deux points d’entrée (main.py) :
```text
project/
│
├── main.py
├── requirements.txt
│
└── blog/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── hashing.py
    ├── token.py
    └── routers/
        ├── auth.py
        ├── user.py
        ├── blog.py
```
---

## Explication de la structure

### main.py (racine)
Fichier de test ou ancien entrypoint.  
Il n’est pas utilisé pour lancer l’application principale.

### blog/main.py (ENTRYPOINT PRINCIPAL)
C’est le vrai point de départ de l’API FastAPI.  
C’est ce fichier qui est exécuté avec Uvicorn :

uvicorn blog.main:app --reload --port 8000

---

### database.py
Configuration de la base de données et session SQLAlchemy.

### models.py
Définition des tables de la base de données.

### schemas.py
Validation des données avec Pydantic.

### hashing.py
Gestion du hashage des mots de passe avec bcrypt.

### token.py
Création et validation des tokens JWT.

---

## routers/

Séparation des routes par fonctionnalité.

### auth.py
Authentification (login + JWT).

### user.py
Gestion des utilisateurs.

### blog.py
CRUD des blogs.

## Flux d’authentification

Client → envoie email + mot de passe  
→ vérification utilisateur en base de données  
→ vérification du mot de passe hashé  
→ génération d’un JWT token  
→ retour du token au client  

## Base de données et sécurité

SQLite utilisée pour le stockage des données. SQLAlchemy utilisé comme ORM pour gérer les tables et relations. Les mots de passe sont hashés avec bcrypt avant stockage. L’authentification est gérée avec JWT pour sécuriser les routes sensibles.

## Comment récupérer et lancer le projet

### 1. Cloner le projet
git clone <url_du_repo>

### 2. Se placer dans le dossier
cd <nom_du_projet>

### 3. Créer un environnement virtuel
python -m venv blog-env

### 4. Activer l’environnement virtuel
Windows PowerShell :
.\blog-env\Scripts\Activate.ps1

Windows CMD :
blog-env\Scripts\activate

### 5. Installer les dépendances
pip install -r requirements.txt

### 6. Lancer le serveur
uvicorn blog.main:app --reload --port 8000

## Accès API

http://127.0.0.1:8000
