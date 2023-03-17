def choice(round_score, my_score, opponent_score):
    if opponent_score <= round_score:
        if round_score <= 17:
            return True
        if round_score >= 17:
            return False
    if opponent_score >= round_score:
        if round_score <= 12:
            return True
        if round_score >= 12:
            return False
