from datetime import datetime
import subprocess
import time

NOM_WIFI = "Wi-Fi"

def desactiver_internet():
    subprocess.run([
        "powershell",
        "-Command",
        f'Disable-NetAdapter -Name "{NOM_WIFI}" -Confirm:$false'
    ])

def activer_internet():
    subprocess.run([
        "powershell",
        "-Command",
        f'Enable-NetAdapter -Name "{NOM_WIFI}" -Confirm:$false'
    ])

def internet_devrait_etre_actif():
    maintenant = datetime.now()

    if maintenant.hour >= 9 and maintenant.hour < 11 and maintenant.weekday() <= 4:
        return True
    else:
        return False

if internet_devrait_etre_actif():
    print("ON")
else:
    print("OFF")        

print("Test dans 3 secondes...")
time.sleep(3)

desactiver_internet()

print("Wi-Fi désactivé!")
time.sleep(10)

activer_internet()

print("Wi-Fi réactivé!")
# python internet_police.py