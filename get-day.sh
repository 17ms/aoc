#!/usr/bin/env bash

[ "$(date +%m)" -ne 12 ] && echo "It's not December yet!" && exit 1
[ "$(date +%H)" -lt 7 ] && echo "It's too early!" && exit 1

DAY=$(date +%d)

[ -d "day$DAY" ] && echo "Day already exists!" && exit 1

mkdir "day$DAY" && cd "day$DAY" && touch "solution.py"
echo -e "#!/usr/bin/env python3\n\nwith open(\"input.txt\", encoding=\"utf-8\") as f:\n    lines = f.read().splitlines()\n" > "solution.py"

echo "[+] Directory and files for day $DAY created"

if ! [ -f "../.cookies/aoc.cookie" ]
then
  echo "Can't find the cookies!"
  exit 1
fi

curl "https://adventofcode.com/$(date +%Y)/day/${DAY//0}/input" \
  -H "Cookie: session=$(cat ../.cookies/aoc.cookie)" \
  -o "input.txt"

echo "[+] Input downloaded to input.txt"
