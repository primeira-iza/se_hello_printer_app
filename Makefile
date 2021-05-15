.PHONY: test

deps:
	pip install -r requirements.txt;
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

test_smoke:
	curl --fail 127.0.0.1:5000

run:
	python main.py

lint:
	flake8 hello_world test

docker_build:
	docker build -t hello-world-printer .

docker_run: docker_build
	docker run \
	--name hello-world-printer-dev \
	-p 5000:5000 \
	-d hello-world-printer

# Zastąp wsbtester1 swoim użytkownikiem hub.docker.com
USERNAME=izawen
TAG=$(USERNAME)/hello-world-printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;
