class Vector():
    'This is a custom made vector class'
    def __init__(self, *coords) -> None:
        self.coords = coords
        if not all(isinstance(coord, int) or isinstance(coord, float) for coord in self.coords):
            wrongTypes = [type(coord) for coord in self.coords if type(coord) != int and type(coord) != float]
            raise TypeError(
                f'Unsupported type, {str(wrongTypes[0])[7:-1]}, in object creation'
            )
        self.len = len(self.coords)


    def __repr__(self) -> str:
        return f'Vector{self.coords}'

    
    def __neg__(self):
        return Vector(*(-coord for coord in self.coords))


    def __pos__(self):
        return Vector(*self.coords)


    def __abs__(self):
        return pow(sum(coord**2 for coord in self.coords), 0.5)


    def __invert__(self):
        'Compute a vector that is orthogonal to this one'
        if self.len <= 1:
            raise TypeError(
                f'Cannot invert vector of len {self.len}.'
                )
        
        nonzero = [0, 1]
        for i, val in enumerate(self.coords):
            if val and i not in nonzero:
                nonzero.append(i)
                nonzero.pop(0)

        newCoords = [coord for coord in self.coords]
        newCoords[nonzero[0]], newCoords[nonzero[1]] = newCoords[nonzero[1]], -newCoords[nonzero[0]]
        return Vector(*(coord if i in nonzero else 0 for i, coord in enumerate(newCoords)))
    

    def __add__(self, other):
        if isinstance(other, Vector):
            newCoords = [0 for i in range(max(self.len, other.len))]   
            newCoords = [self.coords[i] + val if i < self.len else val for i, val in enumerate(newCoords)]
            newCoords = [other.coords[i] + val if i < other.len else val for i, val in enumerate(newCoords)]
            return Vector(*newCoords)
        return NotImplemented


    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(*(self+(-other)).coords)
        return NotImplemented


    def __mul__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord * other for coord in self.coords))
        elif isinstance(other, Vector):
            if self.len == other.len == 3:
                a1, a2, a3 = self.coords
                b1, b2, b3 = other.coords
                i = a2 * b3 - a3 * b2
                j = a1 * b3 - a3 * b1
                k = a1 * b2 - a2 * b1
                return Vector(i, -j, k)
            elif self.len == other.len == 7:
                raise NotImplementedError(
                    f'Cross product in R7 not yet implemented'
                )
            else:
                raise ValueError(
                    f'You can only get a cross product in three and seven dimensional space'
                )
            
            
            return Vector()
        return NotImplemented
     
        
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord / other for coord in self.coords))
        return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented


    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord ** other for coord in self.coords))
        return NotImplemented

    def __rpow__(self, other):
        return NotImplemented
    

    def __matmul__(self, other) -> int:
        'Compute the scalar product between two vectors'
        if not isinstance(other, Vector):
            raise TypeError(
                f'Cannot calculate scalar product with {str(type[other])[7:-1]}.'
            )
        elif self.len != other.len:
            raise ValueError(
                f'Vectors need to have the same number of elemnts.'     
            )
        else:
            return sum(self.coords[i] * other.coords[i] for i in range(self.len))



x = Vector(1, 2, 3)
y = Vector(4, 5, 6)
z = Vector(7, 8, 9)

w = x -y

print(x)
print(y)
print(z)
print(-y) 
print(abs(x))
print(z ** 2)
print(~z)
print(x @ ~x)
print(x * x)
print(x * y)
print(y.__doc__)