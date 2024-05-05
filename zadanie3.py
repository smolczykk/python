class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def pobierz_tytul(self):
        return self.tytul

    def ustaw_tytul(self, nowy_tytul):
        self.tytul = nowy_tytul

    def pobierz_autora(self):
        return self.autor

    def ustaw_autora(self, nowy_autor):
        self.autor = nowy_autor

    def pobierz_rok_wydania(self):
        return self.rok_wydania

    def ustaw_rok_wydania(self, nowy_rok_wydania):
        self.rok_wydania = nowy_rok_wydania