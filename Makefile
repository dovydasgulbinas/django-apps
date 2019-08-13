include .env

TAG = local:$(IMG_NAME)
REPO_REMOTE = $(REPO_OWNER)/$(IMG_NAME)
TAG_REMOTE = $(REPO_REMOTE):$(IMG_VERSION)
CNAME = $(IMG_NAME) 

test:
	coverage run manage.py test bmbhelper -v 2

serve: open
	python manage.py runserver

shell:
	python manage.py shell

open:
	open http://localhost:$(PORT)/$(APP_URI)

freeze:
	pip freeze > requirements.txt
	git add requirements.txt


### DOCKER SECTION ###

remake: rebuild 
rebuild: rm-container rm-image build

rm-container: stop-container
	docker rm $(CNAME) || true

rm-image: rm-container
	docker image rm $(TAG) || true

stop-container:
	docker stop $(CNAME) || true

build:
	docker build --tag $(TAG) .

image-push-remote: remake image-add-remote-tag
	docker image push $(TAG_REMOTE)

image-add-remote-tag:
	docker image tag $(TAG) $(TAG_REMOTE)

comp-build-up: comp-build comp-up

comp-build:
	docker-compose build 

comp-up:
	docker-compose up -d

comp-logs:
	docker-compose logs -f