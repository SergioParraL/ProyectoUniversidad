from django import template 

register = template.Library() 

def concat_Momento(Gradonum): 
    Momentos_list = [
        
        ('I'),
        ('II'),
        ('III'),
    ]  

    Momento = Gradonum - 1
    select_Momento = Momentos_list[Momento]

    return select_Momento

register.filter("concat_Momento",concat_Momento)

