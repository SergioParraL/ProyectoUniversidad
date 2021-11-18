from django import template 

register = template.Library() 

def concat_Tipo(Gradonum): 
    Docs_tipo = [
        
        ('Boletin'),
        ('Constancia'),
        ('Planilla'),
        ('Convocatoria'),
        ('Otro'),
    ]
    Tipo = Gradonum - 1
    select_Tipo = Docs_tipo[Tipo]

    return select_Tipo

register.filter("concat_Tipo",concat_Tipo)

