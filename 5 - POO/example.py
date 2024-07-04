def announcer_decorator(func):
    def wrapper(*args, **kwargs):
        print("O jogo está prestes a começar!")
        result = func(*args, **kwargs)
        print("O jogo acabou! Obrigado por assistir!")
        return result
    return wrapper

@announcer_decorator
def show_score(home_team, away_team, home_score, away_score):
    print(f"{home_team} {home_score} - {away_team} {away_score}")

# Chamar a função decorada
show_score("Flamengo", "Vasco", 3, 1)
