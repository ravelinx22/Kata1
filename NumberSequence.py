class NumberSequence:
    def elementMaxMin(self, cadena):
        if cadena == "":
            return [0, None]
        elif len(cadena) == 1:
            return [len(cadena.split(",")), 1]
        else:
            return [len(cadena.split(",")), 0]
