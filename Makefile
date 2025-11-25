# Variables del proyecto
APP_NAME=maldonado
IMAGE_NAME=ghcr.io/alejandromgt52/maldonado
VERSION=1.0.5
STACK_NAME=quintob
STACK_FILE=stack.yml

# Construcción local de la imagen
build:
	docker build -t $(APP_NAME):$(VERSION) .

# Tag para GitHub Container Registry
tag:
	docker tag $(APP_NAME):$(VERSION) $(IMAGE_NAME):$(VERSION)
	docker tag $(APP_NAME):$(VERSION) $(IMAGE_NAME):latest

# Login a GitHub Container Registry
login:
	@echo "Ingresa tu GitHub Personal Access Token:"
	@docker login ghcr.io -u alejandromgt52

# Push a GitHub Container Registry
push: tag
	docker push $(IMAGE_NAME):$(VERSION)
	docker push $(IMAGE_NAME):latest

# Construcción completa (build + tag + push)
publish: build tag push
	@echo "✅ Imagen publicada: $(IMAGE_NAME):$(VERSION)"

# Pull de la imagen desde GHCR
pull:
	docker pull $(IMAGE_NAME):$(VERSION)

# Desplegar el stack en Docker Swarm
deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

# Eliminar el stack
rm:
	docker stack rm $(STACK_NAME)

# Ver servicios del stack
ps:
	docker service ls | grep $(STACK_NAME)

# Ver logs de un servicio
logs:
	docker service logs -f $(STACK_NAME)_maldonado-app

# Actualizar el servicio (sin downtime)
update: pull
	docker service update --image $(IMAGE_NAME):$(VERSION) $(STACK_NAME)_maldonado-app

# Reiniciar completamente el stack
restart: rm
	@echo "⏳ Esperando a que se detengan los servicios..."
	sleep 30
	make deploy
	@echo "✅ Stack reiniciado"

# Ver estado de los contenedores
status:
	docker ps | grep $(APP_NAME)

# Limpiar imágenes antiguas
clean:
	docker image prune -f
	docker system prune -f

# Ejecutar tests localmente
test:
	python -m unittest test_app.py -v

# Ejecutar la app localmente (sin Docker)
run:
	python app.py

# Ayuda - Mostrar comandos disponibles
help:
	@echo "📋 Comandos disponibles:"
	@echo ""
	@echo "  make build       - Construir imagen Docker localmente"
	@echo "  make tag         - Etiquetar imagen para GHCR"
	@echo "  make login       - Login a GitHub Container Registry"
	@echo "  make push        - Subir imagen a GHCR"
	@echo "  make publish     - Build + Tag + Push (todo en uno)"
	@echo "  make pull        - Descargar imagen desde GHCR"
	@echo "  make deploy      - Desplegar stack en Docker Swarm"
	@echo "  make rm          - Eliminar stack"
	@echo "  make ps          - Ver servicios del stack"
	@echo "  make logs        - Ver logs del servicio"
	@echo "  make update      - Actualizar servicio sin downtime"
	@echo "  make restart     - Reiniciar stack completamente"
	@echo "  make status      - Ver contenedores activos"
	@echo "  make clean       - Limpiar imágenes antiguas"
	@echo "  make test        - Ejecutar tests"
	@echo "  make run         - Ejecutar app localmente"
	@echo "  make help        - Mostrar esta ayuda"

# Comando por defecto
.DEFAULT_GOAL := help