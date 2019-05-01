# Term colors
export TERM="screen-256color"

# Powerlevel9k configuration
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv status context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()
POWERLEVEL9K_STATUS_CROSS=true
POWERLEVEL9K_ALWAYS_SHOW_CONTEXT=false
POWERLEVEL9K_CONTEXT_TEMPLATE="%n"
POWERLEVEL9K_VCS_GIT_HOOKS=(vcs-detect-changes git-tagname)

# System vars
export ALTERNATE_EDITOR='vi'
export EDITOR='emacsclient -t'            # $EDITOR should open in terminal
export VISUAL='emacsclient -c -a emacs'   # $VISUAL opens in GUI with non-daemon as alternate
