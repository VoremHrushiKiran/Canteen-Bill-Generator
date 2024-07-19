import pandas as pd
import bill_maker
c= bill_maker.Canteen()
Breakfast = { 'Items' : [i[0] for i in c.breakfast_menu],
              'Price' : [i[1] for i in c.breakfast_menu],
              }
Veg_starters = { 'Items' : [i[0] for i in c.veg_starters_menu],
                'Price' : [i[1] for i in c.veg_starters_menu],
              }
Veg_biryani = { 'Items' : [i[0] for i in c.veg_biryani_menu],
              'Price' : [i[1] for i in c.veg_biryani_menu],
              }
Non_veg_starters = { 'Items' : [i[0] for i in c.non_veg_starters_menu],
              'Price' : [i[1] for i in c.non_veg_starters_menu],
              }
Non_veg_biryani = { 'Items' : [i[0] for i in c.non_veg_biryani_menu],
              'Price' : [i[1] for i in c.non_veg_biryani_menu],
              }
Fastfood = { 'Items' : [i[0] for i in c.fast_food_menu],
              'Price' : [i[1] for i in c.fast_food_menu],
              }

print('\n1 : BREAKFAST ')
print(pd.DataFrame(Breakfast))
print('\n2 : VEG STARTERS ')
print(pd.DataFrame(Veg_starters))
print('\n3 : VEG BIRYANI ')
print(pd.DataFrame(Veg_biryani))
print('\n4 : NON-VEG STARTERS ')
print(pd.DataFrame(Non_veg_starters))
print('\n5 : NON-VEG BIRYANI ')
print(pd.DataFrame(Non_veg_biryani))
print('\n6 : FAST FOOD ')
print(pd.DataFrame(Fastfood))



