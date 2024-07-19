import bill_maker
import csv
import importlib
importlib.reload(bill_maker)
def main() :

    while True :
        print(
"""            Enter 0 for MENU
            Enter -1 to exit """)

        code = list(map(int,input('Ente the item code :').split('.')))
        if len(code)==1 and code[0]==-1 :
            print('\n','😊'*10,'  THANK YOU  ','😊'*10)
            print('\t\t\tHAVE A NICE DAY')
            break
        canteen= bill_maker.Canteen()
        if len(code)==1 and code[0]==0 :
            canteen.print_menu()
            continue
        elif len(code)%3!=0 :
            # print('entered code doesn\'t contain sufficient elements')
            print('\t\tINVALID INPUT')
            continue
        else :
            count=len(code)//3
            try :

                for i in range(count) :
                    if code[3*i]==1 :
                        canteen.breakfast(code[3*i+1],code[3*i+2])
                    elif code[3*i+0]==2 :
                        canteen.veg_starters(code[3*i+1],code[3*i+2])
                    elif code[3*i+0]==3 :
                        canteen.veg_biryani(code[3*i+1],code[3*i+2])
                    elif code[3*i+0]==4 :
                        canteen.non_veg_starters(code[3*i+1],code[3*i+2])
                    elif code[3*i+0]==5 :
                        canteen.non_veg_biryani(code[3*i+1],code[3*i+2])
                    elif code[3*i+0]==6 :
                        canteen.fast_food(code[3*i+1],code[3*i+2])


            except :
                print("\n\t\t-->COULD'NT FIND ENTERED ITEM")
                print('\t\t-->PLEASE TRY AGAIN\n')
                continue

        canteen.print_bill()
        canteen.save_data()
        # canteen = None


            

if __name__ == "__main__":
    try :
        f = open("Data.csv",'r')
    except :
        f = open("Data.csv", 'x')
        writer = csv.writer(f)
        writer.writerow(["DATE","BILL NO","ITEMS","TOTAL"])
        writer.writerow([0,0,0,0])

    finally:
        f = open("Data.csv", 'r')
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1:
                bill_maker.Canteen.bill_no = row[1]
            else:
                continue
        f.close()
    main()
