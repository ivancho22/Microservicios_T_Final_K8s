# Microservicio de Ventas - Proyecto Final K8s

Este proyecto implementa un **microservicio de ventas** utilizando las tecnologías mencionadas a continuación:

![image](https://github.com/user-attachments/assets/73774ab3-c330-407b-860a-9d12a4c4676d)


## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) - Backend del microservicio en Python
- [Docker](https://www.docker.com/) - Creación de la imágen del microservicio
- [DockerHub](https://hub.docker.com/) - Publicación de la imágen
- [Helm](https://helm.sh/) - Gestión de charts/templates para despliegue en Kubernetes
- [Kubernetes](https://kubernetes.io/) - Orquestación de contenedores
- [Argo CD](https://argo-cd.readthedocs.io/) - GitOps para despliegue continuo, sincronizando cambios con clúster
- [GitHub Actions](https://github.com/features/actions) - CI/CD automatizado y sincronizado con Argo CD

---

## Estructura del proyecto

```
T_Final_K8s/
│
├── app/                     # Microservicio en FastAPI
│   ├── main.py              # Código fuente
│   ├── infoo.py             # Info del sistema (extra)
│   ├── static/style.css     # Estilos del frontend
│   └── templates/index.html # Vista HTML principal
│
├── charts/ventas/          # Chart Helm para el microservicio
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
│
├── argocd/ventas-app.yaml  # Definición de aplicación Argo CD
├── .github/workflows/      # GitHub Actions pipeline
│   └── deploy.yml
│
├── Dockerfile              # Docker build
├── requirements.txt        # Dependencias/librerias de Python
└── .gitignore
```

---

## Pasos para ejecutar localmente

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/T_Final_K8s.git
   cd T_Final_K8s
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta localmente:
   ```bash
   uvicorn app.main:app --reload --port 3030
   ```

4. Abrir en navegador: [http://localhost:3030](http://localhost:3030)

---

## Build y Push a Docker Hub

```bash
docker build -t UsuarioDockerHub/ventas:latest .
docker push UsuarioDockerHub/ventas:latest
```

---

## Despliegue en Kubernetes con Helm

```bash
helm install ventas-chart charts/ventas
```

---

## GitOps con Argo CD

1. Agrega el repo a Argo CD
2. Apunta al archivo `argocd/ventas-app.yaml`
3. Argo CD sincroniza los charts Helm y despliega el microservicio automáticamente

---

## CI/CD con GitHub Actions

Cada `commit` en `main`:
- Construye la imagen Docker
- Hace `push` a Docker Hub

Archivo del pipeline: `.github/workflows/deploy.yml`

---
