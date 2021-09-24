class Build():
    def __init__(self, cart = []):
        self.cart = cart

    def addItem(self, add):
        if add not in self.cart:
            print(f"{add} has been added to the Cart!")
            return self.cart.append(add)
        else:
            print("This item is already in the cart...")
    def showItem(self):
        print("Items in your cart:")
        for s in self.cart:
            print(s)
        if len(self.cart) > 0:    
            return "End of cart." 
        else:
            return "Nothing in the cart."     

    def deleteItem(self, dele):
        if dele in self.cart:
            self.cart.remove(dele)
            print(f"{dele} has been deleted from the Cart!")
        else:
            print("Item not in cart!")

    def clearCart(self):
        self.cart = []


def cart_Logic():
    cart_1 = Build()

    while True:
        user_input = input("What would you like to do? Add/View/Delete or clear Cart: ").lower().strip()
        if user_input == 'quit':
            break
        if user_input == 'view':
            print({cart_1.showItem()})
        if user_input == 'add':
            my_item = input("Enter an item to add to your cart: ")
            cart_1.addItem(my_item)
        if user_input == 'delete':
            my_item = input("Enter an item to delete from your cart: ")
            cart_1.deleteItem(my_item)
        if user_input == 'clear':
            cart_1.clearCart()
            print("Cart has been cleared!")


cart = cart_Logic()
