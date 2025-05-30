## ****** TEST WITH BUSINESS LOGIC (INSERT, UPDATE, DELETE)

from fastapi import FastAPI, Request, Response, HTTPException
from prometheus_client import (
    Counter, Histogram, Summary, Gauge,
    generate_latest, CONTENT_TYPE_LATEST
)
from fastapi.responses import JSONResponse
import time
import random
import psutil

app = FastAPI()

# ─────────────── MÉTRICAS ───────────────

# Solicitudes HTTP
REQUEST_COUNT = Counter(
    'http_requests_total', 'Total de solicitudes HTTP',
    ['method', 'endpoint', 'http_status']
)

# Latencia por endpoint
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds', 'Duración de solicitudes HTTP',
    ['endpoint']
)

# Solicitudes en curso
IN_PROGRESS = Gauge(
    'in_progress_requests', 'Solicitudes en proceso'
)

# Duración de tareas internas simuladas
TASK_DURATION = Summary(
    'task_duration_seconds', 'Duración de una tarea simulada'
)

# Conteo de operaciones de negocio
BUSINESS_LOGIC_COUNTER = Counter(
    'business_logic_calls_total', 'Ejecución lógica de negocio',
    ['operation']
)

# Errores HTTP detallados
ERROR_COUNTER = Counter(
    'http_errors_total', 'Errores HTTP',
    ['endpoint', 'http_status']
)

# Estado de disponibilidad del servicio
SERVICE_AVAILABILITY = Gauge(
    'service_availability', 'Disponibilidad del microservicio (1=UP, 0=DOWN)'
)

# Última solicitud
LAST_REQUEST_TIME = Gauge(
    'last_request_timestamp_seconds', 'Timestamp de la última solicitud'
)

# Usuarios activos simulados
USERS_ACTIVE = Gauge(
    'active_users', 'Usuarios activos simulados'
)

# Recursos del sistema
MEMORY_USAGE = Gauge(
    'memory_usage_bytes', 'Uso de memoria (RSS)'
)
CPU_USAGE = Gauge(
    'cpu_usage_percent', 'Uso de CPU (%)'
)

# Tamaños de solicitudes y respuestas
REQUEST_SIZE = Histogram(
    'http_request_size_bytes', 'Tamaño de las peticiones HTTP',
    ['endpoint']
)
RESPONSE_SIZE = Histogram(
    'http_response_size_bytes', 'Tamaño de las respuestas HTTP',
    ['endpoint']
)

# Conteo por grupo de código de estado
STATUS_GROUP = Counter(
    'http_status_group_total', 'Respuestas por grupo de estado',
    ['status_group']
)

# ─────────────── MIDDLEWARE ───────────────
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    IN_PROGRESS.inc()
    LAST_REQUEST_TIME.set(start_time)
    SERVICE_AVAILABILITY.set(1)  # Disponible mientras se atiende la solicitud

    try:
        # Tamaño del request
        request_body = await request.body()
        REQUEST_SIZE.labels(endpoint=request.url.path).observe(len(request_body))
    except Exception:
        pass

    try:
        response: Response = await call_next(request)
        status_code = response.status_code
        status_group = f"{status_code // 100}xx"
        STATUS_GROUP.labels(status_group=status_group).inc()
    except Exception:
        status_code = 500
        ERROR_COUNTER.labels(endpoint=request.url.path, http_status=500).inc()
        STATUS_GROUP.labels(status_group="5xx").inc()
        raise
    finally:
        IN_PROGRESS.dec()
        process_time = time.time() - start_time
        REQUEST_LATENCY.labels(endpoint=request.url.path).observe(process_time)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            http_status=status_code
        ).inc()

        # Registrar errores explícitos 4xx y 5xx
        if status_code >= 400:
            ERROR_COUNTER.labels(endpoint=request.url.path, http_status=status_code).inc()

        # Tamaño del response
        if hasattr(response, "body") and response.body:
            RESPONSE_SIZE.labels(endpoint=request.url.path).observe(len(response.body))

        # Actualizar métricas del sistema
        update_system_metrics()

    return response

# ─────────────── ENDPOINTS SIMULACIÓN ERRORES ───────────────
@app.get("/error-4xx")
def error_4xx():
    raise HTTPException(status_code=400, detail="Error simulado 4xx")

@app.get("/error-5xx")
def error_5xx():
    raise HTTPException(status_code=500, detail="Error simulado 5xx")

# ─────────────── ENDPOINT DE NEGOCIO ───────────────
@app.get("/")
def read_root():
    op_type = random.choice(["read", "write", "update"])
    BUSINESS_LOGIC_COUNTER.labels(operation=op_type).inc()
    simulated_task()
    simulate_user_activity()
    return {"message": f"Operación {op_type} ejecutada"}

# NUEVO ENDPOINT: carga ligera de CPU
@app.get("/burn-cpu")
def burn_cpu(duration: float = 1.0):
    start = time.time()
    while time.time() - start < duration:
        _ = sum(i * i for i in range(3000))
    return {"message": f"CPU utilizada ligeramente por {duration} segundos"}

@TASK_DURATION.time()
def simulated_task():
    # Simula carga ligera de CPU durante ~0.3s
    end = time.time() + 0.3
    while time.time() < end:
        sum(i * i for i in range(1000))

def simulate_user_activity():
    USERS_ACTIVE.set(random.randint(5, 50))

def update_system_metrics():
    process = psutil.Process()
    MEMORY_USAGE.set(process.memory_info().rss)
    ##CPU_USAGE.set(process.cpu_percent(interval=0.2))
    # Simula variación artificial de CPU
    real_cpu = process.cpu_percent(interval=None)
    simulated_cpu = real_cpu + random.uniform(1, 60)  # suma aleatoria entre 1% y 60%
    CPU_USAGE.set(simulated_cpu)
# ─────────────── ENDPOINT DE MÉTRICAS ───────────────
@app.get("/metrics")
def metrics():
    try:
        update_system_metrics()
        SERVICE_AVAILABILITY.set(1)
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    except Exception:
        SERVICE_AVAILABILITY.set(0)
        raise



##**** Exec STEPS: May 28th ****
# 1) start mic in cmd with > "uvicorn main:app --host 0.0.0.0 --port 8000"   #(Press CTRL+C to quit)  
# 1.1) Verify in>> http://localhost:8000/metrics
# 2) Exec Prometheus local and validate in http://localhost:9090/ . Prom is capturing mic metrics
# 3) Exec Grafana http://localhost:3000/ and check if prometheuse measures are being captured. 

## Config STEPS:
# Install Grafana and Prometheus locally.
# Call metrics endpoint in Prometheus > http://localhost:8000/metrics
# New DSource in Grafanana pointing to Prometheus http://localhost:9090/