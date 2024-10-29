[![CI - Docker Build & Push](https://github.com/xXBlackMasterXx/github-actions-workflows-demo/actions/workflows/docker-push.yml/badge.svg?branch=main)](https://github.com/xXBlackMasterXx/github-actions-workflows-demo/actions/workflows/docker-push.yml)

# GitHub Actions Workflows Demo 🚀

Demostración del uso de flujos de trabajo con GitHub para tuberías de Integración Continua (CI), Entrega Continua (CD) y Despliegue Continuo (CD).

## Azure Container Registry - Push 🚀

Compila y envía una nueva imagen al registro de contenedores de Azure Container Registry

### Variables y Secretos requeridos

| Secreto           | Descripción                                      |
|--------------------|--------------------------------------------------|
| `AZURECR_PASSWORD` | Contraseña de Azure Container Registry           |
| `AZURECR_URI`      | URI del servidor de Azure                        |
| `AZURECR_USERNAME` | Usuario del registro de contenedores             |

---


## GitHub Container Registry - Push 🐙

Compila y envía una nueva imagen al registro de contenedores de GitHub

### Variables y Secretos requeridos

| Secreto | Descripción |
|----------|-------------|
| `TOKEN`  | Access Token de la cuenta de GitHub con permisos de escritura al registro de contenedores de GitHub |