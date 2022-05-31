from django import template 

register = template.Library() 


def concat_Foto(Foto):



    if Foto:
        foto=Foto.url

    else:
        foto='../../../../Institucion/static/General/img/Perfil_Default.jpg'

    return foto

register.filter("concat_Foto",concat_Foto)


