# dotfiles

Keep Linux configuration files for various modules and programs for fast deployment to new machines.


### Deploying dotfiles

Run `deploy.sh`, which orchestrates:

* Running the pex binary that provides the `doit` orchestration tool.
* Installing Powerline fonts if required
* Sourcing `~/.zshrc` for _some_ feedback on success


```sh
./doit
```


### Others


Pex generation:

```sh
pex --compile --python=python3 -r deploy/requirements.txt -m doit -o doit
```
