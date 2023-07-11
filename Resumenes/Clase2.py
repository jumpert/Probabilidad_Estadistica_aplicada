A= {1,2,3}
O= {1,2,3,4,5,6}
def prob_A(A,O):
    prob_A= A/O
    return prob_A

print (f"Y este sera nuestro resultado: {'%.2f' % prob_A(3,6)}")


 #IMPARES   
C={1,3,5}
O= {1,2,3,4,5,6}
def prob_C(C,O):
    prob_C= C/O
    return prob_C

print (f"#IMPARES. Y este sera nuestro resultado: {'%.2f' % prob_C(3,6)}")


#IMPARES MENORES O IGUALES A 3

def prob_C(prob_C,prob_A):
    prob_C= prob_A/prob_C
    return prob_C

print (f"#IMPARES MENORES O IGUALES A 3. Y este sera nuestro resultado: {'%.2f' % prob_C(3,2)}")


#PRIMERAS PROPIEDADES
def prob_A_dado_B(prob_B, prob_A_y_B):
    prob_A_dado_B = prob_B/prob_A_y_B
    return prob_A_dado_B


print (f"#PRIMERAS PROPIEDADES. Y este sera nuestro resultado: {'%.2f' % prob_A_dado_B(2,4)}")

def prob_A_dado_B(prob_B, prob_A1):
    prob_A_dado_B = prob_B/prob_A1
    return prob_A_dado_B


print (f"#PRIMERAS PROPIEDADES. Y este sera nuestro resultado: {'%.2f' % prob_A_dado_B(1,3)}")
