export TAP_NAME=$(shell python setup.py --name)
export TAP_VERSION=$(shell python setup.py --version)

lint:
	flake8 tap_conversor

# To run this step make sure to create config vars on bitbucket
create_config:
	echo "{\"username\":\"$(USERNAME)\",\"password\": \"$(PASSWORD)\",\"start_date\":\"2017-01-01T00:00:00Z\"}" > config.json

test: create_config
	python3 -m unittest discover

# Public techindicium/TAP_NAME:TAP_VERSION (requires TAP_NAME)
build_tap:
	docker build -f Dockerfile -t techindicium/$(TAP_NAME):$(TAP_VERSION) -t techindicium/$(TAP_NAME):latest --build-arg TAP_NAME=$(TAP_NAME)  --build-arg TAP_FOLDER=$(subst -,_,$(TAP_NAME)) .
	docker save --output tmp-image.docker techindicium/$(TAP_NAME):$(TAP_VERSION)

publish_tap: build_tap
	docker login -u $(DOCKER_HUB_USER) -p $(DOCKER_HUB_PASSWORD)
	docker load --input ./tmp-image.docker
	docker push techindicium/$(TAP_NAME):$(TAP_VERSION)
	docker push techindicium/$(TAP_NAME):latest