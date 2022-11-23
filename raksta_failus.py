"""
Mapē /saraksti ieraksta sarakstus ar katras klases skolēniem, kas dosies ekskursijā
"""

def raksta_failus(skoleni_pa_klasem: dict) -> None:
    for klase in skoleni_pa_klasem:

        # veido failu ar doto nosaukumu, piemēram, 11c.txt
        with open("jauns_fails.txt", "w", encoding="UTF-8") as jauns_fails:

            pass 
            # TODO: ieraksta failā visus klases skolēnus katru jaunā rindā

        return None
