bottles = int(99)

while bottles >= 0:
    if bottles > 1:
        print("{} bottles of beer on the wall, {} bottles of beer. \nTake one down and pass it around, {} bottles of beer on the wall.\n".format(bottles,bottles,bottles-1))
    elif bottles == 1:
        print("{} bottles of beer on the wall, {} bottles of beer. \nTake one down and pass it around, no more bottles of beer on the wall.\n".format(bottles,bottles))
    elif bottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.")
    bottles -= 1
