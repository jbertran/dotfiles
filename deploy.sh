#!/usr/bin/zsh

# setup directories
GITDIR_PREFIX='git'

dotfile_dir=`pwd`
repo_dir=$dotfile_dir/..

home=(
    '.gitconfig'
    '.gitignore-global'
    '.i3'
    '.config/termite'
    '.sh_aliases'
    '.spacemacs'
    '.tmux.conf'
    '.zlogin'
    '.zshenv'
    '.zshrc'
)

gitdirs=('perso' 'work')

echo 'Building directories...'
for i in $gitdirs; do
    mkdir -p "$HOME/$GITDIR_PREFIX/$i";
done

echo 'Deploying .files...'
for i in $home; do
    ln -nsf $dotfile_dir/$i ~/$i;
    echo -e "\t$i deployed."
done

echo 'Installing .emacs.d...'
git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d

# get tmux theme pack
[ ! -d "$repo_dir/tmux-themepack" ] && git clone https://github.com/jimeh/tmux-themepack.git $repo_dir/tmux-themepack
ln -nsf $repo_dir/tmux-themepack/ ~/.tmux-themepack

# patch fonts for oh-my-zsh
read -sq $'PWL_CHOICE?Would you like to install Powerline fonts? [N/y]\n'
if [[ "$PWL_CHOICE" = "y" ]]; then
    git clone https://github.com/powerline/fonts $repo_dir/fonts
    sh $repo_dir/fonts/install.sh && rm -rf $repo_dir/fonts
    ([ -d "$repo_dir/fonts" ] && echo "Error in removing powerline fonts") || echo "Powerline fonts installed, don't forget to change shell fonts!"
fi

# terminal color theme setup
read -sq $'SHC_CHOICE?Would you like to install a terminal color theme? [N/y]\n'
if [[ "$SHC_CHOICE" = "y" ]]; then
    git clone git@github.com:Mayccoll/Gogh.git $repo_dir/gogh && $repo_dir/gogh/gogh.sh
fi

echo ''

cd ~ && source ~/.zshrc
