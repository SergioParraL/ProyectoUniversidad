from django import template 

register = template.Library() 

def concat_Formato(Gradonum): 
    Docs_format = [
        
        ('Word'),
        ('Excel'),
        ('PowerPoint'),
        ('PDF'),
        ('LibreOffice'),
        ('Otro'),
    ]

    Format = Gradonum - 1
    select_Format = Docs_format[Format]
    return select_Format

register.filter("concat_Formato",concat_Formato)

