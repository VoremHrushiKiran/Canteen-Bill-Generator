from tabulate import tabulate
import datetime
from datetime import date
import csv
class Canteen :
    bill_no = '0'
    def __init__(self):
        self.breakfast_menu = [
            ['Dosa-Masala', 25],
            ['Dosa-Onion', 25],
            ['Dosa-Plain', 25],
            ['Idly', 25],
            ['Poori', 30],
            ['Upma', 30],
            ['Utappa', 25],
            ['Vada', 30],
            ]
        self.veg_starters_menu = [
            ['Veg manchuria',149],
            ['Veg Spring Roll',149],
            ['Chilli Spring Roll',149],
            ['Mushroom 65',199],
            ['Paneer Manchuria',199],
        ]
        self.veg_biryani_menu =[
            ['Veg Biryani-Mini',179],
            ['Veg Biryani-Regular',219],
            ['Veg Biryani-Large',319],
            ['Paneer Biryani',319],
            ['Paneer Lollipop Biryani',339],
            ['Mushroom Biryani',339],
        ]
        self.non_veg_starters_menu = [
            ['Chicken 65',179],
            ['Chicken Manchuria',149],
            ['Chicken Spring Roll',209],
            ['Chile Fish',289],
            ['Appolo Fish',289],
            ['Prawns Fry',289],
        ]
        self.non_veg_biryani_menu = [
            ['Chicken Biryani-Mini',200],
            ['Chicken Biryani-Regular',379],
            ['Chicken Biryani-Large', 559],
            ['Fish Biryani',359],
            ['Paneer Biryani',359],
            ['Egg Biryani',159],
            ['Egg Masala Biryani',179],
        ]
        self.fast_food_menu = [
            ['Chicken Noodles-Single',70],
            ['Chicken Noodles-Full', 120],
            ['Egg Noodles-Single',60],
            ['Egg Noodles-Full',100],
        ]
        self.total = 0
        self.bill = []
    def breakfast(self,item_code,quantity):
        self.bill.append([self.breakfast_menu[item_code][0],quantity,self.breakfast_menu[item_code][1]*quantity])
        self.total+=self.breakfast_menu[item_code][1]*quantity

    def veg_starters(self,item_code,quantity):
        self.bill.append([self.veg_starters_menu[item_code][0],quantity,self.veg_starters_menu[item_code][1]*quantity])
        self.total += self.veg_starters_menu[item_code][1]*quantity

    def veg_biryani(self,item_code,quantity):
        self.bill.append([self.veg_biryani_menu[item_code][0],quantity,self.veg_starters_menu[item_code][1]*quantity])
        self.total+=self.veg_starters_menu[item_code][1]*quantity

    def non_veg_starters(self,item_code,quantity):
        self.bill.append([self.non_veg_starters_menu[item_code][0],quantity,self.non_veg_starters_menu[item_code][1]*quantity])
        self.total+=self.non_veg_starters_menu[item_code][1]*quantity

    def non_veg_biryani(self,item_code,quantity):
        self.bill.append([self.non_veg_biryani_menu[item_code][0],quantity,self.non_veg_biryani_menu[item_code][1]*quantity])
        self.total+=self.non_veg_biryani_menu[item_code][1]*quantity

    def fast_food(self,item_code,quantity):
        self.bill.append([self.fast_food_menu[item_code][0],quantity,self.fast_food_menu[item_code][1]*quantity])
        self.total+=self.fast_food_menu[item_code][1]*quantity

    def print_bill(self):
        disc=0
        Canteen.bill_no = int(Canteen.bill_no)+1
        print('\n')
        print('='*8,'\tCANTEEN NAME \t','='*8)
        print('\n',"DATE : ",datetime.date.today(),'\t' ,"BILL NO : ",Canteen.bill_no,'\n')
        print(tabulate(self.bill, headers=["Item", "Quantity", "Ammount"]))
        print('_'*30)
        # if date.today()== '2022-08-29'
        if date.today() == date(2022, 8, 29):
            disc=self.total*0.10
            print('TOTAL BILL :\t',self.total)
            print("DISCOUNT : ",disc)
            print('BILL AFTER DISCOUNT :',self.total-disc)
        else :
            print('TOTAL BILL :\t',self.total)
        print('\n','='*8,' 😊THANK YOU😊 ','='*8)
        print('=' * 8, ' 😊VISIT AGAIN😊 ', '=' * 8,'\n','\n')

    def print_menu(self):
        print('\nBREAKFAST:')
        print(tabulate(self.breakfast_menu, headers=["Item", "Price"]))
        print('\nVEG STARTERS :')
        print(tabulate(self.veg_starters_menu, headers=["Item", "Price"]))
        print('\nVEG BIRYANI :')
        print(tabulate(self.veg_biryani_menu, headers=["Item", "Price"]))
        print('\nNON VEG STARTERS :')
        print(tabulate(self.non_veg_starters_menu, headers=["Item", "Price"]))
        print('\nNON VEG BIRYANI :')
        print(tabulate(self.non_veg_biryani_menu, headers=["Item", "Price"]))
        print('\nFAST FOOD :')
        print(tabulate(self.fast_food_menu, headers=["Item", "Price"]))

    def save_data(self):
        with open("Data.csv", 'a') as file :
            writer = csv.writer(file)
            writer.writerow([datetime.date.today(),Canteen.bill_no,self.bill,self.total])




