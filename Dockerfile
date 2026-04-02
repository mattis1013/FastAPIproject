FROM python:3.10

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet
COPY blog/ ./blog

# Lancer le main.py dans le dossier blog
CMD ["python", "blog/main.py"]