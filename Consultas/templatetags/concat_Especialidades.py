from django import template 

register = template.Library() 


def concat_Especialidades(Gradonum):
    Especialidades_list = [
        
        ('Desarrollo Endogeno'),
        ('Educación Física'),
        ('Música'),
        ('Teatro'),
        ('Danza'),
        ('Manualidades'),
        ('Aula Integrada'),
        ('Producción'),
        ('CRA (Centro de Recursos para el Aprendizaje)'),
    ] 

    Esp = Gradonum - 1
    select_esp = Especialidades_list[Esp]

    return select_esp

register.filter("concat_Especialidades",concat_Especialidades)


