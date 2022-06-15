import random
basic3 = [
    "avid",
    "robust",
    "malady",
    "discrement",
    "flounder",
    "jocular",
    "snide",
    "moot",
    "quandary",
    "apprehension",
    "inclement",
    "patronize",
    "pithy",
    "plodding",
    "impede",
    "meander",
    "consumate",
    "archaic",
    "proponent",
    ""
]

shouldGenerate = True

while shouldGenerate:
    y = input("To exit press Y ")
    if (y.lower() == "y"):
        shouldGenerate = False
    else:
        randomNumber = random.randint(0, len(basic3)-1)
        print(basic3[randomNumber])
