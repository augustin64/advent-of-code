# advent-of-code

Add this to your `.bashrc`:
```bash
AOC_PATH=$HOME/path/to/this/repo/
alias aoc="$AOC_PATH/utils/cli.py"
aoc-new () {
  cd $AOC_PATH
  PATH="$PATH:$AOC_PATH"
  $AOC_PATH/new_day.sh
  PS1="$PS1[aoc] "
}
```