import random as rd
import numpy as np

outcome = {}
exec = {}

for infa in range(8):
    for infd in range(6):
        for cava in range(8):
            for cavd in range(2):
                for chiefa in [True, False]:
                    for chiefd in [True, False]:
                        for plain in [True, False]:
                            for i in range(infa):
                                for j in range(infd):
                                    for k in range(cava):
                                        for l in range(cavd):
                                            outcome[((infa, infd, 0, 0, chiefa, chiefd, plain, False), (i, j, k, l, False))] = 0
                            exec[(infa, infd, 0, 0, chiefa, chiefd, plain, False)] = 0

for infa in range(6):
    for cavd in range(4):
        for plain in [True, False]:
            for i in range(infa):
                for l in range(cavd):
                    outcome[((infa, infd, 0, 0, False, False, plain, True), (i, 0, 0, l, True))] = 0
                exec[(infa, infd, 0, 0, False, False, plain, True)] = 0
                outcome[((infa, infd, 0, 0, False, False, plain, True), (i, 0, 0, l, False))] = 0


def side(inf, cav, chief, plain):
    killany = 0
    kill = 0

    for k in range(inf):
        dice = rd.randint(1,6)
        if dice==6 or (chief and dice==5):
            killany +=1
        if plain and (dice==5 or (chief and dice==4)):
            kill +=1

    for k in range(cav):
        dice = rd.randint(1,6)
        if dice==6 or (chief and dice==5):
            killany +=1
        if plain and (dice==5 or dice==4 or (chief and dice==3)):
            kill +=1

    return (killany, kill)


def casualties(inf, cav, killany, kill):
    if killany > cav:
        newcav = 0
        newinf = inf- killany + cav - kill
    else:
        newcav = cav - killany
        newinf = inf - kill
    return (max(0, newinf), newcav, (killany > 0 or (kill > 0 and inf > 0)))



def simbattle(infa, infd, cava, cavd, chiefa, chiefd, plain, fort):
    exec[(infa, infd, cava, cavd, chiefa, chiefd, plain, fort)] += 1
    const = True
    while const:
        (killanya, killa) = side((infa, cava, chiefa), plain)
        if fort:
            (killanyd, killd) = side((infd+1, cavd, chiefd), True)
        else:
            (killanyd, killd) = side((infd, cavd, chiefd), True)

        if fort:
            if killanya > cavd or (plain and killanya == cavd and killa>0):
                infd = cavd = 0
                newfort = False
            else:
                cavd -= killanya
        else:
            (infd, cavd, casud) = casualties(infd, cavd, killanya, killa)
            (infa, cava, casua) = casualties(infa, cava, killanyd, killd)
        const = not (casud or casua)

    return (infa, infd, cava, cavd, fort)



"""for infa in range(8):
    for infd in range(6):
        for it in range(1000):"""