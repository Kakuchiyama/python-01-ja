def counter():
    #occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    apple = ["apple" for fruits in fruits if fruits == "apple" ]
    banana = ["banana" for fruits in fruits if fruits == "banana" ]
    orange = ["orange" for fruits in fruits if fruits == "orange" ]
    grape = ["grape" for fruits in fruits if fruits == "grape" ]
    kiwi = ["kiwi" for fruits in fruits if fruits == "kiwi" ]
    melon = ["melon" for fruits in fruits if fruits == "melon" ]
    strawberry = ["strawberry" for fruits in fruits if fruits == "strawberry" ]
    
    
    occurrences = {
        "apple": len(apple),
        "banana" : len(banana),
        "orange" : len(orange),
        "grape" : len(grape),
        "kiwi" : len(kiwi),
        "melon" : len(melon),
        "strawberry" : len(strawberry)
    }


    return occurrences

print(counter())
