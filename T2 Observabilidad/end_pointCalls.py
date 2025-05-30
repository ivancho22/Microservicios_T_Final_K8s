import requests
import time
#import psutil

BASE_URL = "http://localhost:8000"
DURATION_SECONDS = 15 * 60  # 5 minutos

def call_endpoint(path):
    url = f"{BASE_URL}{path}"
    try:
        response = requests.get(url)
        print(f"GET {path} -> Status: {response.status_code}")
        try:
            print("Response JSON:", response.json())
        except Exception:
            print("No JSON en response")
    except Exception as e:
        print(f"Error calling {path}: {e}")

if __name__ == "__main__":
   # psutil.Process().cpu_percent(interval=None)
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        if elapsed > DURATION_SECONDS:
            print("Tiempo total de ejecución alcanzado. Terminando script.")
            break

        print(f"=== Llamada a endpoints (tiempo transcurrido: {int(elapsed)} s) ===")
        call_endpoint("/")          # Endpoint principal
        call_endpoint("/error-4xx") # Error 4xx simulado
        call_endpoint("/error-5xx") # Error 5xx simulado
        call_endpoint("/burn-cpu?duration=1.0") # CPU% Usage simulado
        print("Esperando 15 segundos...\n")
        time.sleep(15)
