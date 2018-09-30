class NumberSequence:
    def elementMaxMin(self, cadena):
        if cadena == "":
            return [0]
        elif len(cadena) > 1:
            return [2]
        else:
            return [1]
