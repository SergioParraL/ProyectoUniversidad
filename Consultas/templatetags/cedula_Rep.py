from django import template


register = template.Library() 

def cedula_Rep(Rep): 

    nombreRep=Rep.nombres
    cedulaRep=Rep.cedula

    result= f'{nombreRep}|{cedulaRep}'
 

    return result

register.filter("cedula_Rep",cedula_Rep)

