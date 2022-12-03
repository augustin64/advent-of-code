[[ $1 ]] || set -- $(date +%d)
[[ $2 ]] || set -- $1 $(date +%Y)

if [[ ! -e .git ]]; then
	echo "Merci de se déplacer dans le répertoire approprié"
	exit 0
fi;

DAY="$1"
YEAR="$2"
FILENAME="${YEAR}/day${DAY}.py"

python utils/cli.py download -y $YEAR -d $DAY
python utils/cli.py show -y $YEAR -d $DAY

cp utils/template.py "$FILENAME"
sed -i "s/DAY/${DAY}/" "$FILENAME"
sed -i "s/YEAR/${YEAR}/" "$FILENAME"
