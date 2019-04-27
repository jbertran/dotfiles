.PHONY: docker-tests docker-clean

test-name := dotfiles-test
test-distro := centos:7

docker-tests: container-run
	docker run --detach --name $(test-name) $(test-distro)
	pushd ../ansible
	ansible-playbook -i docker-test.yaml playbook_dotfiles.yaml
	popd

docker-clean:
	docker kill $(test-name)
	docker rm $(test-name)

vagrant-tests:
	vagrant up
	pushd ../ansible
	ansible-playbook -i vagrant-test.yaml playbook_dotfiles.yaml
	popd
