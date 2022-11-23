"""
Par darbībām ar failiem Python valodā
https://www.w3schools.com/python/python_file_handling.asp

Par tipu anotācijām
https://realpython.com/lessons/type-hinting/
"""

from ielasa_failu import ielasa_failu as ielasa_f
from karto_datus import atlasa_klases, grupe_pa_klasem
from raksta_failus import raksta_failus

faila_saturs = ielasa_f("skoleni.txt")
tuksas_klases = atlasa_klases(faila_saturs)
skoleni_pa_klasem = grupe_pa_klasem(tuksas_klases, faila_saturs)
raksta_failus(skoleni_pa_klasem)