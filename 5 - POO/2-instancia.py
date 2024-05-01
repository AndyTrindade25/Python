class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
    
# Primeiro Filme #
movie = Movie()
movie.name = "SuperMario Bros"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 60
print("Dados do Filme")
print(f"Nome do filme: {movie.name}")