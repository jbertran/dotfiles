# dotfiles

Automated environment setup for yours truly using Ansible

## Requirements

* `ansible`
* A root-capable user on the target system(s)
* A route to the outside world from the target system(s)

## Usage

```shell
$ ansible-playbook -i <your_inventory> ansible/dotfiles_playbook.yaml
```

## E2E manual tests

Because I'm lazy and Molecule looks like too much work

### Docker

```'shell'
$ docker run --detach --name dotfiles-test -it <your_target_os>
$ ansible-playbook -i ansible/docker-test.yaml ansible/dotfiles_playbook.yaml
```

### Vagrant

Vagrantfile provided in tests, matching inventory at `ansible/vagrant-test.yaml`.

## TODO

