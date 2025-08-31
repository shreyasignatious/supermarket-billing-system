from datetime import datetime

# Customer name input
name = input("ENTER YOUR NAME: ")

# Available items with prices
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggi': 50,
    'boost': 90,
    'colgate': 85
}

item_list_display = '''
RICE     RS 20/KG
SUGAR    RS 30/KG
SALT     RS 20/KG
OIL      RS 80/LITER
PANEER   RS 110/KG
MAGGI    RS 50/KG
BOOST    RS 90/KG
COLGATE  RS 85/EACH
'''

# Show item list
option = int(input("FOR LIST OF ITEMS PRESS 1:"))
if option == 1:
    print(item_list_display)

# Initialize variables
pricelist = []
totalprice = 0
ilist = []
qlist = []
plist = []

# Item input loop
while True:
    item = input("\nENTER YOUR ITEM (or type 'exit' to quit): ").lower()
    if item == 'exit':
        break

    if item in items:
        quantity = int(input("ENTER QUANTITY: "))
        price = quantity * items[item]
        pricelist.append((item, quantity, items[item], price))
        totalprice += price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        print(f"{item.upper()} added to cart. Price: Rs {price}")
    else:
        print("SORRY, THE ITEM YOU ENTERED IS NOT AVAILABLE.")
        continue

    # Ask to bill after each item
    bill = input("CAN I BILL THE ITEMS? (yes/no): ").lower()
    if bill == 'yes':
        break  # exit the loop and show bill
    # if no, continue to next item entry

# Final billing
if totalprice > 0:
    gst = round((totalprice * 5) / 100, 2)
    finalamount = totalprice + gst

    print("\n" + "=" * 27 + " SHREYAS  ESSENTIALS " + "=" * 27)
    print("{:^74}".format("LB-NAGAR"))

    
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    name_line = "NAME: {:<20}".format(name)
    spacing = 75 - len(name_line) - len("DATE: " + date_str)
    print(name_line + " " * spacing + "DATE: " + date_str)

    print("-" * 75)
    print("{:<6} {:<20} {:<20} {:>24}".format("S.No", "ITEM", "QUANTITY", "PRICE"))

    for i in range(len(pricelist)):
        print("{:<6} {:<20} {:<20} {:>24}".format(i + 1,ilist[i].upper(),str(qlist[i]),f"Rs {plist[i]:.2f}"))

    print("-" * 75)
    print("{:>62} Rs {:>7.2f}".format("TOTAL AMOUNT:", totalprice))
    print("{:>62} Rs {:>7.2f}".format("GST (5%):", gst))
    print("-" * 75)
    print("{:>62} Rs {:>7.2f}".format("FINAL AMOUNT:", finalamount))
    print("-" * 75)
    print("{:^75}".format("THANK YOU FOR VISITING!"))
    print("-" * 75)
else:
    print("NO ITEMS WERE PURCHASED.")
