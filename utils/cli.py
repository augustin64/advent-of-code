#!/usr/bin/python3
"""
Interface en ligne de commande pour interagir avec https://adventofcode.com/
Prérequis: fichier ~/.aoc-cookie contenant le cookie de connexion au site
Suggéré: alias aoc="$CHEMIN_VERS_CE_REPO/utils/cli.py"
"""
from optparse import OptionParser
from pathlib import Path
import datetime
import colors
import os

import requests
from bs4 import BeautifulSoup



home = str(Path.home())
with open(os.path.join(home, ".aoc-cookie"), "r", encoding='utf8') as file:
    cookie = file.read().replace("\n", " ").strip()

session = requests.Session()
session.cookies["session"] = cookie


def download_input(year, day):
    """Télécharge la donnée d'entrée correspondant à un certain jour"""
    request = session.get(f"https://adventofcode.com/{year}/day/{int(day)}/input")
    with open(f"{year}/inputs/day{str(day).zfill(2)}.txt", "w", encoding='utf8') as file:
        file.write(request.content.decode())
    print("ok")


def show_puzzle(year, day, part=None, colored=False):
    """Affiche l'énoncé du jour demandé"""
    request = session.get(f"https://adventofcode.com/{year}/day/{int(day)}")

    content = request.content.decode("utf-8")
    if colored:
        content = content.replace("<h2", f"{colors.bold}<h2")
        content = content.replace('<em class="star">', f'<em class="star">{colors.bold}{colors.yellow}')
        content = content.replace('<em>', f'<em>{colors.bold}')
        content = content.replace('<a href', f'{colors.green}<a href')
        content = content.replace("</h2>", f"</h2>{colors.reset}\n")
        content = content.replace("</em>", f"</em>{colors.reset}")
        content = content.replace("</a>", f"</a>{colors.reset}")



    soup = BeautifulSoup(content, "html.parser")
    day_desc = soup.find_all("article", {"class": "day-desc"})
    if part is None:
        for i in range(len(day_desc)):
            print(day_desc[i].text)
        return
    if part > len(day_desc) or part <= 0:
        print(f"Partie {part} non disponible")
        return
    print(day_desc[part - 1].text)


def submit(year, day, answer, level=1):
    """Soumet une réponse à validation"""
    request = session.post(
        f"https://adventofcode.com/{year}/day/{int(day)}/answer",
        data={"answer": answer, "level": level},
    )
    soup = BeautifulSoup(request.content, "html.parser")
    print(soup.find("main").find("article").find("p").text)


def __main__(options, args):
    """Fonction principale"""
    if len(args) == 0:
        print("Une action doit être spécifiée")
        return
    if args[0] == "download" or args[0] == "dl":
        download_input(options.year, options.day)
    elif args[0] == "show" or args[0] == "sh":
        if options.level == "":
            options.level = None
        else:
            options.level = int(options.level)
        show_puzzle(options.year, options.day, options.level, colored=True)
    elif args[0] == "submit" or args[0] == "sb":
        if len(args) < 2:
            answer = input("Answer ?\n>> ")
        else:
            answer = args[1]
        if options.level == "":
            options.level = 1
        submit(options.year, options.day, answer, options.level)
    else:
        print(f"Invalid action {args[0]}")


today = datetime.datetime.now()

USAGE = "usage: %prog (download|dl|show|sh|submit|sb) [options]"
parser = OptionParser(usage=USAGE)
parser.add_option(
    "-y",
    "--year",
    dest="year",
    help="Année",
    action="store",
    default=today.year
)

parser.add_option(
    "-d",
    "--day",
    dest="day",
    help="Jour",
    action="store",
    default=today.day
)

parser.add_option(
    "-l",
    "--level",
    dest="level",
    help="Niveau de la difficulté",
    action="store",
    default=""
)


if __name__ == "__main__":
    (OPTIONS, args) = parser.parse_args()
    __main__(OPTIONS, args)
