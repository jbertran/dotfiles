dotfile_dir=`pwd`
repo_dir=$dotfile_dir/..

home=('.tmux.conf'
      '.emacs' '.emacs.d'
      '.gitconfig' '.gitignore-global'
      '.zshrc' '.sh_aliases' '.sh_env')

for i in $home; do
    ln -nsf $dotfile_dir/$i ~/$i;
done

# oh-my-zsh
[ ! -d "$repo_dir/oh-my-zsh" ] && git clone http://github.com/jbertran/oh-my-zsh $repo_dir/oh-my-zsh
ln -nsf $repo_dir/oh-my-zsh ~/.oh-my-zsh

source ~/.zshrc
