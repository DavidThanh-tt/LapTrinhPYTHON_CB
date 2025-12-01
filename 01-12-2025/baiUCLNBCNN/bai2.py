import Ham_Uc_Bc
import nhapAB

AB = nhapAB.nhapAB()
UCLN = Ham_Uc_Bc.USCLN(AB[0],AB[1])

print(f'UCLN cua {AB[0]} va {AB[1]}: {UCLN}')