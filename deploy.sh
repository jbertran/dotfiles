dotfile_dir=`pwd`

home=('.tmux.conf'
      '.emacs' '.emacs.d'
      '.gitconfig' '.gitignore-global'
      '.zshrc' '.sh_aliases' '.sh_env')

for i in $home; do
    ln -fs $dotfile_dir/$i ~/$i;
done

source ~/.zshrc
