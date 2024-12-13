import tinytuya

# Aufforderung zur Eingabe von Tuya-Anmeldedaten
print("Tuya Account Login")
username = input("Email/Username: ")
password = input("Password: ")
country_code = input("Country Code (z.B. 49 für DE): ")

# Geräteinformationen abrufen
devices = tinytuya.Cloud(
    apiRegion='eu',  # Europa: 'eu', Asien: 'cn', USA: 'us'
    apiKey='Dein_API_Key',
    apiSecret='Dein_API_Secret',
    apiDeviceID='optional_device_id'  # Optional
).device_list()

# Ergebnisse ausgeben
print("Gefundene Geräte:")
for device in devices:
    print(f"Name: {device['name']}, ID: {device['id']}, Local Key: {device['local_key']}")
