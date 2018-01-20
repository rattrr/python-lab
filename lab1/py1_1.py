# -*- coding: utf-8 -*-

print "Cześć, {} jesteś {}".format(raw_input("Podaj imię: "), "niepełnoletni" if raw_input("Podaj wiek: ") < 18 else "pełnoletni")
