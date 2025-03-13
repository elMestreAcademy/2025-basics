import random


def main():
    respuestas = [
        'Es cierto.',                               # 0
        'Es decididamente así.',                    # 1
        'Sin lugar a dudas.',                       # 2
        'Sí, definitivamente.',                     # 3
        'Puedes confiar en ello.',                  # 4
        'Como yo lo veo, sí.',                      # 5
        'Lo más probable.',                         # 6
        'Perspectiva buena.',                       # 7
        'Sí.',                                      # 8
        'Las señales apuntan a que sí.',            # 9
        'Respuesta confusa, vuelve a intentarlo.',  # 10
        'Vuelve a preguntar más tarde.',            # 11
        'Mejor no decirte ahora.',                  # 12
        'No se puede predecir ahora.',              # 13
        'Concéntrate y vuelve a preguntar.',        # 14
        'No cuentes con ello.',                     # 15
        'Mi respuesta es no.',                      # 16
        'Mis fuentes dicen que no.',                # 17
        'Las perspectivas no son muy buenas.',      # 18
        'Muy dudoso.'                               # 19
    ]

    print(random.choice(respuestas))


main()
