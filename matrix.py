import hashlib
import random
import time
import fitz
import argparse
import os

from colorama import Fore
from colorama import Style


class Matrix:
    def __init__(self, sleep_time=0.1, file_name="flaubert_salammbo") -> None:
        """
        You can pimp your phrase, I suggest you to adapt it to the length of your screen
        """
        self.hash_instance = hashlib.sha256()
        self.path_to_pdf = (
            os.path.dirname(os.path.abspath(__file__)) + "\\" + file_name + ".pdf"
        )
        print(self.path_to_pdf)
        self.sleep_time = sleep_time
        self.insert_number = 7
        self.max_space_number = 5
        self.taille_de_la_portion = 100

    def generate_hash(self):
        """
        Génère un hash prêt à être affiché
        """
        random_int = random.randint(1, 1000)
        self.hash_instance.update(bytes(random_int))
        return self.hash_instance.hexdigest()

    def display(self, texte):
        """
        Affiche le texte donné en paramètre avec une marge et des insertions d'espace de taille aléatoire
        """
        marge = random.randint(0, 10)
        texte_spaced = self.insertion(texte)
        full_texte = "     " * marge + texte_spaced
        print(f"{Fore.GREEN} {full_texte} {Style.RESET_ALL}")
        time.sleep(self.sleep_time)

    def insertion(self, texte):
        """
        You can pimp your phrase here.
        """
        for i in range(self.insert_number):
            position = random.randint(0, len(texte))

            space_number = random.randint(1, self.max_space_number + 1)
            espaces = " " * space_number
            if (
                len(texte) == 64
            ):  # si c'est un hash, je trouve plus jolie de rajouter un petit invariant au milieu
                texte_a_inserer = espaces + texte[0 : random.randint(3, 10)] + espaces
            else:
                texte_a_inserer = espaces * 2
            texte = texte[:position] + texte_a_inserer + texte[position:]

        return texte

    def generate_and_display_hash(self):
        """
        To the infinity and beyond !
        """
        while True:
            texte = self.generate_hash()
            self.display(texte)

    def generate_and_display_pdf(self):
        """
        For smart people
        """
        while True:
            # try:
            document = fitz.open(self.path_to_pdf)
            os
            # except fitz.fitz.FileNotFoundError:
            #     raise FileNotFoundError(
            #         f"le pdf {self.path_to_pdf} à afficher n'est pas dans le répertoire"
            #     )

            paquet = ""
            position = 0
            for page_number in range(document.page_count):
                page = document.load_page(page_number)
                texte_page = page.get_text()

                mots = texte_page.split()

                for mot in mots:
                    paquet += mot + " "
                    if len(paquet) >= self.taille_de_la_portion:
                        position += len(paquet)
                        self.display(paquet)
                        paquet = ""

            document.close()

    def screen(self, type="hash"):
        if type == "hash":
            self.generate_and_display_hash()

        elif type == "pdf":
            self.generate_and_display_pdf()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your true form is here")
    parser.add_argument("--pdf", action="store_true", help="read Salammbô")
    parser.add_argument("--hash", action="store_true", help="just display hash")
    parser.add_argument(
        "--sleep",
        type=float,
        help="change the sleep time (0.1 by default)",
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=str,
        help="file in the directory",
    )

    args = parser.parse_args()

    if args.pdf:
        if args.file:
            matrix = Matrix(args.sleep if args.sleep is not None else 0.1, args.file)
        else:
            matrix = Matrix(args.sleep if args.sleep is not None else 0.1)
        type = "pdf"
        matrix.screen(type="pdf")
    elif args.hash:
        matrix = Matrix(args.sleep if args.sleep is not None else 0.1)
        type = "hash"
        matrix.screen(type="hash")
    else:
        matrix = Matrix()
        type = "hash"
        matrix.screen(type="hash")
