#!/usr/bin/env bash

[ "$(date +%m)" -ne 12 ] && echo "[-] It's not December yet!" && exit 1
[ "$(date +%H)" -lt 7 ] && echo "[-] It's too early!" && exit 1

OUTPUT_FILENAME="input.txt"
COOKIE_PATH="../../.cookies/aoc.cookie"
YEAR=$(date +%Y)
DAY=$(date +%d)

[ -d "$YEAR" ] || (mkdir "$YEAR" && echo "[+] Created directory for $YEAR")
cd "$YEAR"

[ -d "day$DAY" ] && echo "[-] Day already exists!" && exit 1

mkdir "day$DAY" && cd "day$DAY" && touch "solution.py"
echo -e "#!/usr/bin/env python3\n\nwith open(\"input.txt\", encoding=\"utf-8\") as f:\n    lines = f.read().splitlines()\n" > "solution.py"

echo "[+] Directory and files for $YEAR/day$DAY created"

if ! [ -f "$COOKIE_PATH" ]
then
  echo "[!] Can't find the cookies!"
  exit 1
fi

if [ "$DAY" -lt 10 ]
then
    URL="https://adventofcode.com/$YEAR/day/${DAY//0}/input"
else
    URL="https://adventofcode.com/$YEAR/day/$DAY/input"
fi

echo "[+] Fetching exercise input from $URL"

curl "$URL" \
  -H "Cookie: session=$(cat "$COOKIE_PATH")" \
  -o "$OUTPUT_FILENAME"

echo "[+] Input downloaded to $OUTPUT_FILENAME"

