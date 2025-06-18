####---- to execute in root pah of the folder solution>> E:\01Especializacion BI UAO\Diplomado USabana\microservicio_ventas_completo>

## 2) Create Image after creating micro >> docker build -t microservicio-ventas:1.0 .
## 2.1) Validate Images was created >> docker images
## 3) Execute the container>> docker run -d -p 3300:80 microservicio-ventas:1.0

# -----*** DOCKER HUB
## 4) Rename local image with the docker user >> docker tag microservicio-ventas:1.0 anderson442/ventas:latest  
#rebuilt image >> docker build -t anderson442/ventas:latest .

## 4.1) Login >> docker login -u anderson442            ##docker login   ## https://login.docker.com/activate    ## 
## 4.2) Push Image to Docker Hub >> docker push anderson442/ventas:latest
## EXECUTE LOCALLY FOR TESTING>> docker run -p 3030:3030 anderson442/ventas:latest

# -----*** Helm Chart  kubectl logs ventas-chart-568b46c9c6-f4xr2

##5) Install Helm Chart > helm install ventas-chart charts/ventas    to update >> helm upgrade ventas-chart charts/ventas
##5.1) check pods and services >> helm list --namespace default 
#kubectl get pods  >>> status must be running
#kubectl get svc
##5.2) check the microservices deployed into Kubernetes http://localhost:30080

# -----*** ARGO CD (Deployment to Kubernetes Cluster)

##6)Create namespace of ArgoCD >>  kubectl create namespace argocd
#6.1) Instal ArgoCD >> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
#6.2) Acces to local Dashboard >> kubectl port-forward svc/argocd-server -n argocd 8080:443
#6.22) Open http://localhost:8080/
#6.23) Get admin user Password in Pshell >> kubectl -n argocd get secret argocd-initial-admin-secret `-o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($_)) }
  
