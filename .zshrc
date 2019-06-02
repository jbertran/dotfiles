# Setup aliases and environment
[ -f ~/.sh_aliases ] && source ~/.sh_aliases

# Setup powerlevel9k
source /usr/share/zsh-theme-powerlevel9k/powerlevel9k.zsh-theme

# Setup venvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/git/work
source /usr/bin/virtualenvwrapper.sh

# Setup nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# tmux $TERM
export TERM='screen-256color'

# Treat # as comment delimiter in interactive lines
setopt INTERACTIVE_COMMENTS

# bash-style word movement
export WORDCHARS=''
autoload -U select-word-style
select-word-style bash

# Ctrl-Arrow combinations
bindkey '^[[1;5D' emacs-backward-word
bindkey '^[[1;5C' emacs-forward-word
bindkey '^H' backward-delete-word

setopt histignorealldups sharehistory

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

# Home/end fuckup between zsh and tmux
bindkey "^[[1~" beginning-of-line
bindkey "^[[4~" end-of-line

# ZSH completion options
zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'
