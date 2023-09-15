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
pyenv init - | source
