#ship - координата корабля
#x - переменная шагающая по диапазону 1-10
#"wWw" - корабль
#"~" - вода

print("\n")
ship = int(input("Input coordinate of ship(2..8) -"))
print("\n")

for x in range(1,11):
    if x == ship-1:
        print( "wWw", end="" )
    else:
        print( "~", end="" )

print("\n")
