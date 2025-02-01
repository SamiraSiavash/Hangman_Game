import random

image_list = [
    """ 





"""
    , """ 





__________"""
    , """
|
|
|
|
|       
|__________"""
    , """******
|
|
|
|
|       
|__________"""
    , """******
|    |
|    O
|    |
|
|       
|__________"""
    , """******
|    |
|    O
|    |/ 
|
|       
|__________"""
    , """******
|    |
|    O
|   \\|/
|
|       
|__________"""
    , """******
|    |
|    O
|   \\|/
|     \\ 
|       
|__________"""
    , """******
|    |
|    O
|   \\|/
|   / \\ 
|       
|__________"""
]
fruit_list = ["coconut", "pineapple", "watermelon", "kiwi", "strawberry", "lemon", "mango", "grape", "peach",
              "blueberry"]
food_list = ["spaghetti", "sushi", "steak", "fish", "pizza", "sandwich", "chicken", "cheeseburger", "noodles", "bread"]
animal_list = ["lion", "chicken", "tiger", "donkey", "elephant", "crocodile", "monkey", "giraffe", "camel", "kangaroo"]
country_list = ["switzerland", "turkey", "china", "denmark", "australia", "canada", "spain", "unitedstates", "brazil",
                "argentina"]

while True:
    word_list = []
    true_letters = []
    false_letters = []
    result = []

    category_num = int(input("Please enter a category[fruit[1], food[2], animal[3], country[4]]: "))
    match category_num:
        case 1:
            word_list = fruit_list
            category = "Fruit"
        case 2:
            word_list = food_list
            category = "Food"
        case 3:
            word_list = animal_list
            category = "Animal"
        case 4:
            word_list = country_list
            category = "Country"
        case _:
            print("Invalid number.")
            break

    word = random.choice(word_list)
    for i in range(len(word)):
        result += "_"
    print(f"{category}: {result}")

    while len(false_letters) <= 7:
        if "_" in result:
            letter = (input("\nPlease enter a letter: ")).lower()
            while letter in true_letters or letter in false_letters or len(letter) != 1:
                letter = (input("Please enter another letter: ")).lower()
            if letter in word:
                true_letters.append(letter)
                count = word.count(letter)
                index = 0
                if count > 1:
                    for j in range(0, count):
                        index = word.index(letter, index)
                        result.pop(index)
                        result.insert(index, letter)
                        index += 1
                    print(f"{category}: {result}\nTrue letters: {true_letters}\nFalse letters: {false_letters}\n")
                    if len(false_letters) > 0:
                        print(image_list[len(false_letters)])
                else:
                    index = word.index(letter, index)
                    result.pop(index)
                    result.insert(index, letter)
                    print(f"{category}: {result}\nTrue letters: {true_letters}\nFalse letters: {false_letters}\n")
                    if len(false_letters) > 0:
                        print(image_list[len(false_letters)])
            else:
                false_letters.append(letter)
                print(f"{category}: {result}\nTrue letters: {true_letters}\nFalse letters: {false_letters}\n")
                print(image_list[len(false_letters)])
        else:
            print(f"Answer is: {word}\nYou win!")
            break
    else:
        print(f"Answer is: {word}\nGame over!")

    if input(f"\nDo you want play again?[Y,N]: ").upper() == "N":
        print("Goodbye.")
        break
