class NumberSequence:
    def elementMaxMin(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        else:
            nums = list(map(int, cadena.split(",")))
            if len(nums) == 1:
                return [len(nums), min(nums), max(nums), 1]
            else:
                return [len(nums), min(nums), max(nums), sum(nums)/len(nums)]
