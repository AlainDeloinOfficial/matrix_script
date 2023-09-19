import hashlib
import random
import time
import fitz

from colorama import Fore
from colorama import Style


class Matrix:
    def __init__(self) -> None:
        self.hash_instance = hashlib.sha256()
        self.path_to_pdf = "./flaubert_salammbo.pdf"

    def generate_hash(self):
        random_int = random.randint(1, 1000)
        self.hash_instance.update(bytes(random_int))
        return self.hash_instance.hexdigest()

    def generate_pdf(self):
        pass

    def display(self, texte):
        """
        Affiche le texte donné en paramètre avec une marge et des insertions d'espace de taille aléatoire
        """
        marge = random.randint(0, 10)
        texte_spaced = self.insertion(texte)
        full_texte = "     " * marge + texte_spaced
        print(f"{Fore.GREEN} {full_texte} {Style.RESET_ALL}")
        time.sleep(0.1)

    def insertion(self, texte):
        insert_number = 5
        max_space_number = 5
        for i in range(insert_number):
            position = random.randint(0, len(texte))

            space_number = random.randint(1, max_space_number + 1)
            espaces = " " * space_number
            if (
                len(texte) == 64
            ):  # si c'est un hash, je trouve plus jolie de rajouter un petit invariant au milieu
                texte_a_inserer = espaces + texte[0 : random.randint(3, 10)] + espaces
            else:
                texte_a_inserer = espaces * 2
            texte = texte[:position] + texte_a_inserer + texte[position:]

        return texte

    def screen(self, type="hash"):
        if type == "hash":
            while True:
                texte = self.generate_hash()
                self.display(texte)
        elif type == "pdf":
            taille_de_la_portion = 100
            document = fitz.open("./flaubert_salammbo.pdf")
            paquet = ""
            position = 0

            for page_number in range(document.page_count):
                page = document.load_page(page_number)
                texte_page = page.get_text()
                # print("texte_page", texte_page)

                mots = texte_page.split()
                # print("texte_split", mots)

                for mot in mots:
                    paquet += mot + " "
                    if len(paquet) >= taille_de_la_portion:
                        position += len(paquet)
                        # print("position", position)
                        # print(paquet)
                        self.display(paquet)
                        paquet = ""

            document.close()


if __name__ == "__main__":
    matrix = Matrix()
    matrix.screen(type="pdf")
