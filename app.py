import os

# Sengaja menaruh password di dalam kode (celah keamanan)
API_SECRET = "sk_live_1234567890rahasia"

def cek_host(domain):
    # Sengaja rentan Command Injection
    os.system("ping -c 1 " + domain)

cek_host("google.com")