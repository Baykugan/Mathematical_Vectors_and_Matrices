class Matrix():
    'This is a custom made matrix class'
    def __init__(self, *rows):

        self.dict = {}
        self.tDict = {}
        self.n = len(rows)
        self.m = set()
        
        for i, row in enumerate(rows):
            self.m.add(len(row))
            for j, num in enumerate(row):
                coord = (i, j)
                self.dict[coord] = num
            if len(self.m) > 1:
                raise ValueError(
                    f'Rows of different length given, row {i + 1} differing by {max(self.n) - min(self.n)}.'
                )
    
        self.m = int(list(self.m)[0])
        
        if not all(isinstance(val, int) or isinstance(val, float) for key, val in self.dict.items()):
            wrongTypes = [type(val) for key, val in self.dict.items() if type(val) != int and type(val) != float]
            raise TypeError(
                f'Unsupported type, {str(wrongTypes[0])[7:-1]}, in object creation'
            )
            

    def __repr__(self):
        ret = ''
        # ret += f'Matrix{self.m, self.n}\n'
        for i in range(self.n):
            ret += '│'
            for j in range(self.m):
                if j != 0:
                    ret += f', '
                ret += f'{self.dict[(i, j)]}'
            ret += f'│\n'
        return f'{ret}'
    


# ┌
# │
# └


x = Matrix((1, 2, 4), [3, 4, 5], (5, 6, 7))

print(x)
