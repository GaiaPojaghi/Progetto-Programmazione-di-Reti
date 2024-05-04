import subprocess
import platform
import socket

def ping(host):
    """
    Invia un pacchetto ICMP a un host specificato e restituisce True se l'host è raggiungibile, False altrimenti.
    """
    # Verifica il sistema operativo per determinare il comando ping corretto
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Esegue il ping e restituisce True se l'host è raggiungibile, False altrimenti
    try:
        result = subprocess.run(['ping', param, '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"Timeout scaduto durante il ping di {host}")
        return False
    except Exception as e:
        print(f"Errore durante il ping di {host}: {str(e)}")
        return False

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def main():
    """
    Funzione principale per monitorare lo stato degli host.
    """
    # Chiede all'utente di inserire gli indirizzi IP degli host da monitorare
    hosts = input("Inserire gli indirizzi IP degli host da monitorare (separati da virgola): ").split(',')

    # Itera attraverso gli host e controlla il loro stato
    for host in hosts:
        host = host.strip()  # Rimuove eventuali spazi bianchi
        if not is_valid_ip(host):
            print(f"{host} non è un indirizzo IP valido.")
            continue
        
        if ping(host):
            print(f"{host} è online.")
        else:
            print(f"{host} è offline.")

if __name__ == "__main__":
    main()
    