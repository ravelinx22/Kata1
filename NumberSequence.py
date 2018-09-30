class NumberSequence:
    def elementMaxMin(self, cadena):
        if cadena == "":
            return [0, None]
        else:
            return [len(cadena.split(",")), 1]
