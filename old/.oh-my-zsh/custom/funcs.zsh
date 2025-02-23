
stars() {
  case "$1" in
    back) cd ~/Projects/starblazers/backend ;;
    front) cd ~/Projects/starblazers/frontend ;;
    *) echo "Invalid argument. Usage: stars [back|front]" ;;

  esac
}

fn() { 
  file=$(rg --files | fzf) && nvim "$file"
}

rgf() {
  # ripgrep find
  rg --files | fzf
}

cr() {
  # [c]ompile & [r]un provided C file with gcc
  base_name=${1%.*}
  # Run the gcc command
  gcc -o "$base_name" "$1"
  if [ $? -ne 0 ]
  then
    echo "Compilation failed"
  else
    script -q -c "./"$base_name"" /dev/null
  fi
}
