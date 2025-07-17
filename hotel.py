#resturant menu
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

#greeting message
print("Welcome to SANA Resturant")
print("\n Pizza: Rs.40\n Pasta: Rs.50\n Burger: Rs.60\n Salad: Rs.70\n Coffee:Rs.80\n")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")    
                
another_order = input("Do you want to add another item? (yes/no)")
if(another_order == "yes"):
    item_2 = input("Enter the name of second item = ")  
    if item_2 in menu:     
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to order")  
    else:           
        print(f"Ordered item {item_2} is not available yet")   

print(f"The total amount of items to play is {order_total}")         