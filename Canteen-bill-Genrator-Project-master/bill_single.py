from tabulate import tabulate
class Canteen :
    def __init__(self):
        self.total = 0
        self.bill = [['Dosa-Onion', 5, 125]]
    def breakfast(self,item_code,quantity):
        menu=[
            ['Dosa-Masala',25],
            ['Dosa-Onion',25],
            ['Dosa-Plain', 25],
            ['Idly',25],
            ['Poori',30],
            ['Upma',30],
            ['Utappa',25],
            ['Vada',30],
            ]
        self.bill.append([menu[item_code][0],quantity,menu[item_code][1]*quantity])
        self.total+=menu[item_code][1]*quantity
    def print_bill(self):
        print(self.total)

        print(tabulate(self.bill, headers=["Item", "Quantity", "Ammount"]))

    def print_menu(self):
        pass


def main():
    while True:
        print("""
            Enter 0 for item codes
            Enter -1 to exit 
             """)
        code = list(map(int, input('Ente the item code :').split('.')))
        if len(code) == 1 and code[0] == -1:
            break
        canteen = Canteen()
        if len(code) == 1 and code[0] == 0:
            canteen.print_menu()
        elif len(code) % 3 != 0:
            print('entered code doesn\'t contain sufficient elements')
        else:
            count = len(code) % 3

            for i in range(count):
                if code[3 * i] == 1:
                    canteen.breakfast(code[3 * i + 1], code[3 * i + 2])
                elif code[3 * i + 0] == 2:
                    pass
        canteen.print_bill()


if __name__ == "__main__":
    main()