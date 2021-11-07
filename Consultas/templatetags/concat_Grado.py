from django import template 

register = template.Library() 



def concat_Grado(value_1, value_2): 
    a = value_1
    b = int(value_2) - 1

    d = a[b][1]
    return d

register.filter("concat_Grado",concat_Grado)

