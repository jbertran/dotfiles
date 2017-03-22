GITDIR_PREFIX='git'

dotfile_dir=`pwd`
repo_dir=$dotfile_dir/..

home=('.tmux.conf' '.zlogin'
      '.spacemacs' '.emacs.d'
      '.gitconfig' '.gitignore-global'
      '.zshrc' '.sh_aliases' '.sh_env')

gitdirs=('perso' 'work' 'fac')

echo 'Building directories...'
for i in $gitdirs; do
    mkdir -p "$HOME/$GITDIR_PREFIX/$i";
done

echo 'Deploying .files...'
for i in $home; do
    ln -nsf $dotfile_dir/$i ~/$i;
    echo -e "\t$i deployed."
done

# get oh-my-zsh
[ ! -d "$repo_dir/oh-my-zsh" ] && git clone http://github.com/jbertran/oh-my-zsh $repo_dir/oh-my-zsh
ln -nsf $repo_dir/oh-my-zsh/ ~/.oh-my-zsh

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
read -sq $'SHC_CHOICE?Would you like to install a terminal color theme? [N/y]'
if [[ "$SHC_CHOICE" = "y" ]]; then
    wget -O xt https://git.io/vKOB6 && chmod +x xt && ./xt && rm xt
fi

cd ~ && source ~/.zshrc
