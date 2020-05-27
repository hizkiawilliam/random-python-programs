print("Price for Nintendo Wii is Rp. 1500000")
money = int(input("How much money do you have? "))
price = int(1500000)
if money < price:
    print("You need Rp. {} more to buy 1 Nintendo Wii.".format(int(price-money)))
elif money == price:
    print("You can buy 1 Nintendo Wii.")
else:
    nintendo = int(money//price)
    need = int(price-(money%price))
    print("You can buy {} Nintendos, and need Rp. {} more to buy additional Wii.".format(nintendo,need))
