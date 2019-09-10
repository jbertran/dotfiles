#!/usr/bin/zsh

SCRIPT_PATH=$(readlink -f $0)
REPO_DIR=`dirname $SCRIPT_PATH`

echo "<Powerline fonts>"
# patch fonts for oh-my-zsh
read -sq $'PWL_CHOICE?Would you like to install Powerline fonts? [N/y]\n'
if [[ "$PWL_CHOICE" = "y" ]]; then
    git clone https://github.com/powerline/fonts $repo_dir/fonts
    sh $repo_dir/fonts/install.sh && rm -rf $repo_dir/fonts
    ([ -d "$repo_dir/fonts" ] && echo "Error in removing powerline fonts") || echo "Powerline fonts installed, don't forget to change shell fonts!"
fi

echo "<Dotfiles>"
$REPO_DIR/doit deploy || exit 1

echo "<Source .zshrc>"
source ~/.zshrc
