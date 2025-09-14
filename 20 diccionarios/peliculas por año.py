peliculas = {"Titanic": 1997, "Inception": 2010, "The Matrix": 1999, "Interstellar": 2014}
ordenadas = dict(sorted(peliculas.items(), key=lambda x: x[1]))
print(ordenadas)