# Include ~/.local/bin in PATH
export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH

# Term colors
export TERM="screen-256color"

# Powerlevel9k configuration
export POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv status context dir vcs)
export POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()
export POWERLEVEL9K_STATUS_CROSS=true
export POWERLEVEL9K_ALWAYS_SHOW_CONTEXT=false
export POWERLEVEL9K_CONTEXT_TEMPLATE="%n"
export POWERLEVEL9K_VCS_GIT_HOOKS=(vcs-detect-changes git-tagname)

# Debian environment
export DEBFULLNAME="Jordi Bertran de Balanda"
export DEBEMAIL=jordi.bertran@scality.com

# System vars
export ALTERNATE_EDITOR=''
export EDITOR='emacsclient -t'           # $EDITOR should open in terminal
export VISUAL='emacsclient -c -a emacs'   # $VISUAL opens in GUI with non-daemon as alternate
