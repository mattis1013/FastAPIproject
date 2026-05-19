This is the first app i'm working on! welcome guys :)
APP files are inside blog file ie /blog, I would have to delete main.py later and make it more clear

This project is the best way to learn API REST by coding one

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
