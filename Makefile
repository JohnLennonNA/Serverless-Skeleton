ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

up:
	cd Services/${ARGS}/ && sls simulate apigateway -p 5000

lib:
	docker run -it --rm --name installLib -v "$(PWD)/Services/${ARGS}/":/app -w /app python:2.7 pip install -r requirements.txt -b .libs/

deploy:
	cd Services/${ARGS}/ && serverless deploy --stage prod

tests:
	docker run -it --rm --name execTest -v "$(PWD)/Tests":/app -w /app python:2.7 python -m unittest ${ARGS}Test
