.PHONY: run-tests

docker-name := dotfiles-test
docker-file := Dockerfile.test
docker-inv := docker-test.yaml
docker-tag := docker-tester

container-build: $(docker-file)
	docker build -t $(docker-tag) . -f $(docker-file)

container-run: container
	docker run --detach --name $(docker-name) $(docker-tag)

run-tests: container-run
	ansible-playbook -i docker-test.yaml playbook_dotfiles.yaml
