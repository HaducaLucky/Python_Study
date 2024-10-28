
#! format specifiers = {value:flags} format a value based on what flag are inserted

#* .(number)f = round to the many decimal places (fixed point)
#* :(number) = allocate that many spaces
#* :03 = allocate and zero pad that many spaces
#* :< = left justify
#* :> = right justify
#* :^ center align
#* :+ = user a plus sign to indicate positive value
#* := = place sign to leftmost position
#* :  = insert a space before positive numbers
#* :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1212.43

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")