[[ $1 ]] || set -- $(date +%d)
[[ $2 ]] || set -- $1 $(date +%Y)

if [[ ! -e .git ]]; then
	echo "Merci de se déplacer dans le répertoire approprié"
	exit 0
fi;

DAY="$1"
YEAR="$2"
FILENAME="${YEAR}/day${DAY}.py"

cp utils/template.py "$FILENAME"
sed -i "s/DAY/${DAY}/" "$FILENAME"
sed -i "s/YEAR/${YEAR}/" "$FILENAME"
codium "$PWD" "$PWD/$FILENAME"

if [[ $(date +%H) -lt 6 ]]; then
	SECONDS_UNTIL_START=$(( $(date -f - +%s- <<< "today 06:00"$'\nnow') 0 ))
	echo "Waiting ${SECONDS_UNTIL_START} seconds.."
	sleep $SECONDS_UNTIL_START;
fi;
echo "Goooooo !"

python utils/cli.py download -y $YEAR -d $DAY
python utils/cli.py show -y $YEAR -d $DAY