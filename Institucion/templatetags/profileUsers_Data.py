from django import template


register = template.Library() 

def profileUsers_Data(User, condicion): 
    condicion=str(condicion)


    from Institucion.models import PA_profile,PD_profile
    User = User
    if User.is_PA == True:
        if PA_profile.objects.filter(usuario_id=User.id):
            dataPA = PA_profile.objects.get(usuario_id=User.id)

            if dataPA.foto:
                fieldsPA=[
                    dataPA.nombres,
                    dataPA.apellidos,
                    dataPA.cedula,
                    dataPA.cargo,
                    dataPA.foto.url
                ]
                result=fieldsPA[int(condicion)]

            else:
                fieldsPA=[
                    dataPA.nombres,
                    dataPA.apellidos,
                    dataPA.cedula,
                    dataPA.cargo,
                    "../../static/General/img/Perfil_Default.jpg"
                ]
                result=fieldsPA[int(condicion)]
        else:
            fieldsPA=[
                'No actualizado',
                'No actualizado',
                'No actualizado',
                'No actualizado',
                "../../static/General/img/Perfil_Default.jpg"
            ]
            result=fieldsPA[int(condicion)]

        return result

    else:
        if PD_profile.objects.filter(usuario_id=User.id):
            dataPD = PD_profile.objects.get(usuario_id=User.id)

            if dataPD.foto:
                fieldsPD=[
                    dataPD.nombres,
                    dataPD.apellidos,
                    dataPD.cedula,
                    'Docente',
                    dataPD.foto.url
                ]
                result=fieldsPD[int(condicion)]

            else:
                fieldsPD=[
                    dataPD.nombres,
                    dataPD.apellidos,
                    dataPD.cedula,
                    'Docente',
                    "../../static/General/img/Perfil_Default.jpg"
                ]
                result=fieldsPD[int(condicion)]
        else:

            fieldsPD=[
                'No actualizado',
                'No actualizado',
                'No actualizado',
                'No actualizado',
                "../../static/General/img/Perfil_Default.jpg"
            ]
            result=fieldsPD[int(condicion)]

        return result

register.filter("profileUsers_Data",profileUsers_Data)

