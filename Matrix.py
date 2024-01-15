class Matrix():
    'This is a custom made matrix class'
    def __init__(self, *rows, dictionary={}, n=0, m=0):
        self.dict = dictionary.copy()
        self.n = n
        self.m = m

        if len(rows) > 0:
            self.newMatrix(rows)
        elif self.n == 0 or self.m == 0:
            self.n = max([coord[0] for coord in self.dict.keys()]) + 1
            self.m = max([coord[1] for coord in self.dict.keys()]) + 1


        if not all(isinstance(val, int) or isinstance(val, float) for val in self.dict.values()):
            wrongTypes = [type(val) for val in self.dict.values() if type(val) != int and type(val) != float]
            raise TypeError(
                f'Unsupported type, {str(wrongTypes[0])[7:-1]}, in object creation'
            )
            
    
    def newMatrix(self, rows):
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


    def __repr__(self):
        ret = ''
        # ret += f'Matrix{self.n, self.m}\n'
        for i in range(self.n):
            ret += '│'
            for j in range(self.m):
                if j != 0:
                    ret += f', '
                ret += f'{self.dict[(i, j)]}'
            ret += f'│\n'
        return f'{ret}'
    
    def __neg__(self):
        retDict = {}
        for key, val in self.dict.items():
            retDict[key] = -val
        return Matrix(dictionary=retDict, n=self.n, m=self.m)
    
    def __neg__(self):
        retDict = {}
        for key, val in self.dict.items():
            retDict[key] = val
        return Matrix(dictionary=retDict, n=self.n, m=self.m)
    

    def transpose(self):
        retDict = {}
        for key, val in self.dict.items():
            y, x = key
            retDict[(x, y)] = val
        return Matrix(dictionary=retDict, n=self.m, m=self.n)
    


def idMatrix(n):
    return Matrix(*[[1 if i == j else 0 for i in range(n)] for j in range(n)])

def nullMatrix(n, m):
    return Matrix(*[[0 for _ in range(m)] for _ in range(n)])
    

# ┌
# │
# └


x = Matrix((1, 2, 4), [3, 4, 5], (5, 6, 7), (1, 4, 6))
y = nullMatrix(2, 5)
z = Matrix(dictionary=x.dict, n=x.n, m=x.m)
i = idMatrix(4)

print(x)
print(x.transpose())
print(-x)
print(y)
print(z)
print(i)