#!/bin/bash
move()
{
  if [[ $1 == "forward" ]]; then
    pos_x=$((pos_x + $2))
  elif [[ $1 == "up" ]]; then
    pos_y=$((pos_y - $2))
  else
    pos_y=$((pos_y + $2))
  fi;
}

move2()
{
  if [[ $1 == "down" ]]; then
    aim=$((aim + $2))
  elif [[ $1 == "up" ]]; then
    aim=$((aim - $2))
  else
    pos_x=$((pos_x + $2))
    pos_y=$((pos_y + $2*aim))
  fi;
}

part1()
{
  pos_x=0
  pos_y=0
  aim=0
  while read -r action valeur
  do
    move "$action" "$valeur"
  done < "inputs/day02.txt"
  echo "($pos_x, $pos_y): $((pos_x * pos_y))"
}

part2()
{
  pos_x=0
  pos_y=0
  aim=0
  while read -r action valeur
  do
    move2 "$action" "$valeur"
  done < "inputs/day02.txt"
  echo "($pos_x, $pos_y): $((pos_x * pos_y))"
}

echo "Partie 1: $(part1)"
echo "Partie 2: $(part2)"
