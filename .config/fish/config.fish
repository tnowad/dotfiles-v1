export GPG_TTY=$(tty)
set fish_greeting ""
export EDITOR="nvim"

if status is-interactive
  # Commands to run in interactive sessions can go here
end

# tabtab source for packages
# uninstall by removing these lines
[ -f ~/.config/tabtab/fish/__tabtab.fish ]; and . ~/.config/tabtab/fish/__tabtab.fish; or true

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH

# pyenv
# pyenv init - | source

# Jenv
eval set -gx PATH '/home/tnowad/.jenv/shims' $PATH
set -gx JENV_SHELL fish
set -gx JENV_LOADED 1
set -e JAVA_HOME
set -e JDK_HOME
jenv rehash 2>/dev/null
jenv refresh-plugins
function jenv
  set command $argv[1]
  set -e argv[1]

  switch "$command"
  case enable-plugin rehash shell shell-options
    jenv "sh-$command" $argv | source
  case '*'
    command jenv "$command" $argv
  end
end
