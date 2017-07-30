# dotfiles

Keep Linux configuration files for various modules and programs for fast deployment to new machines.

To deploy, just clone and run `deploy.sh`.

## Directory tree

* `dotfiles`
  * `.tmux.conf`
  *`.zlogin`
  *`.spacemacs`
  *`.emacs.d`
  *`.gitconfig`
  *`.gitignore-global`
  *`.zshrc`
  *`.sh_aliases`
  *`.sh_env`
  * `oh-my-zsh` - local clone of [oh-my-zsh clone]().
  * `tmux-themepack` - local clone of [tmux-themepack]()
* `home/<USER>`
  * symlinks for config files
  * git
    * work
    * perso

Optional powerline fonts and terminal color themes repositories are both removed after
their installation is complete.

## WiP

* Package this as a .deb for more install targets and dependencies (zsh etc) - sometimes https
  to the outside is not available too :(
* Get a dummy user going for testing deployment
* Add git 
