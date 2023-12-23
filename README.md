# advent-of-code

## Progress
```
               1111111111222222
      1234567890123456789012345
2020: ***~.....................
2021: *******~~~...............
2022: ***************~.*..*....
2023: **********************~..

.: nothing
~: 1 star
*: 2 stars
```

## Shortcut
Add this to your `.bashrc`:
```bash
AOC_PATH=$HOME/path/to/this/repo/
alias aoc="$AOC_PATH/utils/cli.py"
aoc-new () {
  # To create a new day
  cd $AOC_PATH
  PATH="$PATH:$AOC_PATH"
  $AOC_PATH/utils/new_day.sh
  export PYTHONPATH="$PYTHONPATH:$AOC_PATH"
}

aoc-env () {
  # To load the AoC environment
  cd $AOC_PATH
  PATH="$PATH:$AOC_PATH"
  export PYTHONPATH="$PYTHONPATH:$AOC_PATH"
}
```