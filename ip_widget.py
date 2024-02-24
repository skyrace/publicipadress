import tkinter as tk
from tkinter import ttk
import requests

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        ip = data.get('ip', 'Non Trouvé')
        country = data.get('country', 'Non Trouvé')
        provider = data.get('org', 'Non Trouvé').split(' ')[0]  # Prendre seulement la première partie
        return f"IP : {ip}\nPays : {country}\nFournisseur : {provider}"
    except requests.RequestException:
        return "Erreur: Impossible de récupérer les informations"

# Configuration de base de l'interface graphique
root = tk.Tk()
root.title("IP Public")
root.geometry("500x150")  # Ajustement de la taille pour mieux s'adapter au contenu

# Configuration du style pour des tons plus sombres
style = ttk.Style()
style.theme_use('alt')  # Utilisez un thème alternatif qui est généralement plus sombre
style.configure('TFrame', background='#333333')
style.configure('TLabel', foreground='white', background='#333333', font=('Helvetica', 10))
style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'), background='#333333', foreground='light green')

# Cadre principal
main_frame = ttk.Frame(root, padding="20", style='TFrame')
main_frame.pack(fill=tk.BOTH, expand=True)

# Cadre pour le titre
header_frame = ttk.Frame(main_frame, style='TFrame')
header_frame.pack(fill=tk.X, expand=False)
#header_label = ttk.Label(header_frame, text="Détails de votre connexion Internet", style='Header.TLabel')
#header_label.pack(pady=10)

# Cadre pour les informations
info_frame = ttk.Frame(main_frame, style='TFrame')
info_frame.pack(fill=tk.BOTH, expand=True)

info = tk.StringVar()
info.set("Chargement...")

info_label = ttk.Label(info_frame, textvariable=info, style='TLabel')
info_label.pack(side=tk.TOP, pady=10)

def update_info():
    info.set(get_ip_info())
    root.after(3600000, update_info)  # Mise à jour toutes les heures

update_info()

root.mainloop()
