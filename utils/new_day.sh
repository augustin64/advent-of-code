if [[ ! -e .git ]]; then
	echo "Merci de se déplacer dans le répertoire approprié"
	exit 0
fi;

YEAR=$(date +%Y)
DAY=$(date +%d)
FILENAME="${YEAR}/day${DAY}.py"

cp utils/template.py "$FILENAME"
sed -i "s/DAY/${DAY}/" "$FILENAME"
sed -i "s/YEAR/${YEAR}/" "$FILENAME"
