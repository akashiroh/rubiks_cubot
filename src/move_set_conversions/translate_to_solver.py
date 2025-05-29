def solver_moves(moves: str):
    """
    This function reorders the solver moves to be compatible with rubik-cube
    """
    moves = moves.split()
    
    collect = []
    for move in moves:
        if move[-1] == "'":
            collect.append(
                move[0] + "i"
            )
        elif move[-1] == "2":
            collect.append(move[0])
            collect.append(move[0])
        else:
            collect.append(move[0])

    return " ".join(collect)
