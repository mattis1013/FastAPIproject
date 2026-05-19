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

project/  
├── main.py  
├── database.py  
├── models.py  
├── schemas.py  
├── hashing.py  
├── token.py  
└── routers/  
&nbsp;&nbsp;&nbsp;&nbsp;├── auth.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── user.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── blog.py  


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
