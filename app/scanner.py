import socket
import requests


# 21: FTP (File Transfer Protocol)
# 22: SSH (Secure Shell)
# 23: Telnet (não seguro e raramente usado atualmente)
# 25: SMTP (e-mail)
# 53: DNS (Domain Name System)
# 80: HTTP (não seguro; preferível HTTPS)
# 110: POP3 (e-mail)
# 143: IMAP (e-mail)
# 443: HTTPS (seguro, mas ainda é útil verificar)
# 3306: MySQL (banco de dados)
# 5432: PostgreSQL (banco de dados)
# 5900: VNC (Virtual Network Computing)
# 6379: Redis (muitas vezes não autenticado por padrão)
# 8080: HTTP alternativo (muitas vezes usado para APIs e outros serviços)

def verificar_status(url):
    try:
        response = requests.get(url, timeout=10)
        status = "Online" if response.status_code == 200 else f"Status code: {response.status_code}"
        response_time = round(response.elapsed.total_seconds(),2)
        return status, response_time
    except requests.exceptions.RequestException:
        return "Offline", None


def verificar_portas(host, portas_personalizadas):
    portas_abertas = []

    for porta in portas_personalizadas:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2) # Tempo limite de conexão de 1 segundo para cada porta
            if s.connect_ex((host, porta)) == 0:
                portas_abertas.append(porta) # Porta aberta
    
    return portas_abertas






