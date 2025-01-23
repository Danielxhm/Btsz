import os
import time
from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service

# Cargar las variables de entorno
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
DESTINATION_ADDRESS = os.getenv("DESTINATION_ADDRESS")

if not PRIVATE_KEY or not DESTINATION_ADDRESS:
    raise ValueError("Las variables de entorno PRIVATE_KEY y DESTINATION_ADDRESS son obligatorias.")

# Crear la wallet usando la clave privada
wallet = Wallet.create("mi_wallet", keys=PRIVATE_KEY, network="bitcoin")

# Servicio para interactuar con la blockchain
service = Service(network="bitcoin")

def check_and_send_funds():
    print("Chequeando balance...")
    # Obtener balance de la wallet
    balance = wallet.getbalance()
    print(f"Balance actual: {balance} BTC")

    if balance > 0:
        print(f"Enviando {balance} BTC a {DESTINATION_ADDRESS}...")
        tx = wallet.send_to(DESTINATION_ADDRESS, balance)
        print(f"Transacción completada. ID de la transacción: {tx}")
    else:
        print("No hay fondos disponibles.")

def main():
    print("Iniciando bot...")
    while True:
        try:
            check_and_send_funds()
        except Exception as e:
            print(f"Error detectado: {e}")
        # Esperar 60 segundos antes de volver a revisar
        time.sleep(60)

if __name__ == "__main__":
    main()
