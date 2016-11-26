GITDIR_PREFIX='git'

dotfile_dir=`pwd`
repo_dir=$dotfile_dir/..

home=('.tmux.conf' '.zlogin'
      '.spacemacs' '.emacs.d'
      '.gitconfig' '.gitignore-global'
      '.zshrc' '.sh_aliases' '.sh_env')

gitdirs=('perso' 'work' 'fac')

for i in $gitdirs; do
    mkdir -p "$HOME/$GITDIR_PREFIX/$i";
done

for i in $home; do
    ln -nsf $dotfile_dir/$i ~/$i;
    echo "$i setup complete."
done

# get oh-my-zsh
[ ! -d "$repo_dir/oh-my-zsh" ] && git clone http://github.com/jbertran/oh-my-zsh $repo_dir/oh-my-zsh
ln -nsf $repo_dir/oh-my-zsh/ ~/.oh-my-zsh

# patch fonts for oh-my-zsh
if [ -d "~/.local/share/fonts" ]; then
    git clone https://github.com/powerline/fonts $repo_dir/fonts
    sh $repo_dir/fonts/install.sh && rm -rf $repo_dir/fonts
    ([ -d "$repo_dir/fonts" ] && echo "Error in removing powerline fonts") || echo "Powerline fonts installed, don't forget to change shell fonts!"
else
    echo "Powerline fonts probably already installed"
fi

cd ~ && source ~/.zshrc
