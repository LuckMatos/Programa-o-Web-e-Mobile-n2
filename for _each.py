
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

func_bateram_ameta = 0
fun_nBat_meta = 0
quantidade =len(vendas)
# for e if
for vendas in vendas:
    if vendas>= meta:
        func_bateram_ameta+=1
    elif vendas<meta:
        fun_nBat_meta+=1
        

print(f'A empresa é composta por {quantidade} funcionários, a porcentagem de funcionários que bateram a meta é {func_bateram_ameta/quantidade:.0%}, em relação {fun_nBat_meta/quantidade:.0%} que não bateram  em Agosto')

        
    
    
    
        