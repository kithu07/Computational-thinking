def mod_inverse(modulo : int , num : int) :
    rem1 = modulo
    rem2 = num
    x1 =  y2 = 1
    x2 = y1 = 0
    while rem2 != 1 :
        q = rem1 // rem2
        rem3 = rem2
        rem2 = rem1 - (q*rem2)
        rem1 = rem3
        y1,y2 = y2, y1 - (y2 * q)
        x1,x2 = x2, x1 - (x2 * q)
    return y2 % modulo  
print(mod_inverse(181,14))