# Backpack Class Assignment - Ganesh Baral

class Backpack:
    def __init__(self, color, size, items, open):
        self.color = color
        self.size = size
        self.items = items
        self.open = open

    def openBag(self):
        self.open = True
        print("Your Backpack is now open.")

    def closeBag(self):
        self.open = False
        print("Your backpack is now closed.")

    def putIn(self, item):
        if self.open == True:
            self.items.append(item)
            print(item + " was added to your backpack.")


    def takeOut(self, item):
        if self.open == True:
            self.items.remove(item)
            print(item + " was removed from your backpack.")
        else:
            print("Backpack is not open or item is missing.")

smallBag  = Backpack("Blue", "Small")
mediumBad = Backpack("Red", "Medium")
largeBag  = Backpack("Green", "Large")

smallBag.openBag()
smallBag.putIn("Lunch")
smallBag.putIn("Jacket")
smallBag.closeBag()
smallBag.openBag()
smallBag.takeOut("Jacket")
smallBag.closeBag()