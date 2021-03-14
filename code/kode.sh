#!/bin/bash

N=10000
COUNT=1
MAX=100

while [ "$COUNT" -le $N ]   
do
  number=$RANDOM
  let "number %= $MAX"
  let number=$((($number + 1)))
  echo "$number" >> bash.raw
  COUNT=$((($COUNT + 1)))
done
