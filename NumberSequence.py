class NumberSequence:
    def elementMaxMin(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        else:
            nums = list(map(int, cadena.split(",")))
            return [len(nums), min(nums), max(nums), sum(nums)/len(nums)]
