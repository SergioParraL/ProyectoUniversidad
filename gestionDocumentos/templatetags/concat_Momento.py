from django import template 

register = template.Library() 



def concat_Momento(value_1, value_2): 
    a = value_1
    b = int(value_2) - 1

    d = a[b][3]
    return d

register.filter("concat_Momento",concat_Momento)

