import sys
import random
from pathlib import Path
before_import = set(sys.modules.items())
import sub_modules.converter
after_import = set(sys.modules.items())
print("Which module is just imported? ->", after_import - before_import)


class Dice:
    def __init__(self):
        self.value = 0
    
    def roll(self):
        self.value = random.randint(1, 6)



dices = [Dice(), Dice()]
members = ["Vu", "Truong", "Hieu", "Khoa", "Vinh"]

cur_path = Path("./sub_modules/")
if (cur_path.exists()):
    from sub_modules import converter
    line = converter.collection_to_string(members)
    print(line)

chosen_one = random.choice(members)
print("The chosen one:", chosen_one)
print("The chosen one will roll the dice first")

for dice in dices:
    dice.roll()

print(f"({dices[0].value} {dices[1].value})")