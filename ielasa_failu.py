"""
Ielasa doto teksta failu sarakstā (ignorējot pirmo rindu)
"""

def ielasa_failu(faila_nos: str) -> list:

    faila_saturs = []

    with open(faila_nos, "r", encoding="UTF-8") as fails:

        for rinda in fails:
            pass

            # TODO: ielasa failu rindu pa rindai sarakstā, jāizmanto f-ja strip()

        # TODO: atgriež sarakstu, kur elementu skaits = rindu skaits failā
        return faila_saturs