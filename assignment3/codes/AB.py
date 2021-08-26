BC = 4.5
CD = 5
AD = 5.5
AC = 5.5
BD = 7

def cordinates(PQ, PR, QR):
    p1 = (PQ**2+QR**2-PR**2)/(2*QR)
    return((p1,(PQ**2-p1**2)**(0.5)))

print("B = ", cordinates(BC, BD, CD))
print("A = ", cordinates(AC, AD, CD))

