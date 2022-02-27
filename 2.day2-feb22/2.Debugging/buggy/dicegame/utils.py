class UnnecessaryError(Exception):
    pass


def i_just_throw_an_exception():
    raise UnnecessaryError("\n\nRestart the game. Choose 'y' or 'n' next time ")
