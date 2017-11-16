class PyclubError(Exception):
    pass

class PyclubValueError(PyclubError, ValueError):
    pass

class PyclubTypeError(PyclubError, TypeError):
    pass