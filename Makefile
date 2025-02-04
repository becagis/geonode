# Set variables to pass
DOCKER_HOST := $(DOCKER_HOST)
DOCKER_HOST_IP := `docker run --net=host codenvy/che-ip:nightly`

auto-up:
	# bring up the services with proper environment variables
	unset DOCKERHOST; \
	export DOCKERHOST=$(DOCKER_HOST); \
	echo Docker daemon is running at the following address $$DOCKERHOST; \
	unset GEONODE_LB_HOST_IP; \
	export GEONODE_LB_HOST_IP=$(DOCKER_HOST_IP); \
	echo GeoNode will be available at the following address http://$$GEONODE_LB_HOST_IP; \
	echo If you want to run it on localhost then remember to add this line "localhost $$GEONODE_LB_HOST_IP" to /etc/hosts; \
	docker-compose up -d --build

up:
	docker-compose up -d

build:
	docker-compose build django
	docker-compose build celery

sync: up
	# set up the database tables
	docker-compose exec django django-admin.py migrate --noinput
	docker-compose exec django django-admin.py loaddata sample_admin
	docker-compose exec django django-admin.py loaddata geonode/base/fixtures/default_oauth_apps_docker.json
	docker-compose exec django django-admin.py loaddata geonode/base/fixtures/initial_data.json

migrate:
	django-admin.py migrate --noinput

migrate_setup: migrate
	django-admin.py loaddata sample_admin

wait:
	sleep 5

logs:
	docker-compose logs --follow

down:
	docker-compose down

pull:
	docker-compose pull

smoketest: up
	docker-compose exec django python manage.py test geonode.tests.smoke --noinput --nocapture --detailed-errors --verbosity=1 --failfast

unittest: up
	docker-compose exec django python manage.py test geonode.people.tests geonode.base.tests geonode.layers.tests geonode.maps.tests geonode.proxy.tests geonode.security.tests geonode.social.tests geonode.catalogue.tests geonode.documents.tests geonode.api.tests geonode.groups.tests geonode.services.tests geonode.geoserver.tests geonode.upload.tests geonode.tasks.tests --noinput --failfast

test: smoketest unittest

reset: down up wait sync

hardreset: pull build reset

develop: pull build up sync

# @becagis
## PROD ----------------------------------------------------------------------------
prod-pull:
	docker-compose pull

prod-up:
	docker-compose up

prod-up-daemon:
	docker-compose up -d

prod-down:
	docker-compose down

prod-exec:
	docker-compose exec django bash

prod-publish:
	docker-compose build django
	docker-compose push django

## LDAP
prod-ldap-up:
	docker-compose --project-name geonode-ldap -f docker-compose.yml -f docker-compose-ldap-server.yml up

prod-ldap-down:
	docker-compose --project-name geonode-ldap -f docker-compose.yml -f docker-compose-ldap-server.yml down

prod-ldap-exec:
	docker-compose --project-name geonode-ldap -f docker-compose.yml -f docker-compose-ldap-server.yml exec django bash

## DEV ----------------------------------------------------------------------------
dev-up:
	docker-compose --project-name geonode-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml up -d
	docker-compose --project-name geonode-dev exec django bash -c "python manage.py runserver 0.0.0.0:8000"

dev-down:
	docker-compose --project-name geonode-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml down

dev-exec:
	docker-compose --project-name geonode-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml exec django bash

## LDAP
dev-ldap-up:
	docker-compose --project-name geonode-ldap-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml -f docker-compose-ldap-server.yml up -d
	docker-compose --project-name geonode-ldap-dev exec django bash -c "python manage.py runserver 0.0.0.0:8000"

dev-ldap-down:
	docker-compose --project-name geonode-ldap-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml -f docker-compose-ldap-server.yml down

dev-ldap-exec:
	docker-compose --project-name geonode-ldap-dev -f docker-compose.yml -f .devcontainer/docker-compose.yml -f docker-compose-ldap-server.yml exec django bash