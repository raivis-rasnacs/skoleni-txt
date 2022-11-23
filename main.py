with open("skoleni.txt", "r", encoding="UTF-8") as fails:
    next(fails)
    klases = []
    for rinda in fails:
        klases.append(rinda[rinda.index(" ", rinda.index(" ") + 1):].strip())

    klases = list(dict.fromkeys(klases))
    print(klases)

    fails.seek(0)

    skoleni_pa_klasem = {}
    for klase in klases:
        skoleni_pa_klasem[klase] = []
        for rinda in fails:
            if klase in rinda:
                skoleni_pa_klasem[klase] += [rinda[:rinda.index(" ", rinda.index(" ") + 1)]]
        fails.seek(0)

    print(skoleni_pa_klasem)
    