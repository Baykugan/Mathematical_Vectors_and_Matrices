class Vector():
     
    def __init__(self, *coords) -> None:
        self.coords = coords
        if not all(isinstance(coord, int) or isinstance(coord, float) for coord in self.coords):
            wrongTypes = [type(coord) for coord in self.coords if type(coord) != int and type(coord) != float]
            raise TypeError(
                f'Unsupported type, {str(wrongTypes[0])[7:-1]}, in object creation.'
            )


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
        if len(self) <= 1:
            raise TypeError(
                f'Cannot invert vector of len {len(self)}.'
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
            newCoords = [0 for i in range(max(len(self), len(other)))]   
            newCoords = [self[i] + val if i < len(self) else val for i, val in enumerate(newCoords)]
            newCoords = [other[i] + val if i < len(other) else val for i, val in enumerate(newCoords)]
            return Vector(*newCoords)
        return NotImplemented


    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(*(self+(-other)).coords)
        return NotImplemented


    def __mul__(self, other):
        'Multiplies a scalar and a vector or computes the dot product of two vectors.'
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord * other for coord in self.coords))
        
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError(
                    f'Vectors need to have the same number of elements to calculate dot product.'     
                )
            else:
                return sum(self[i] * other[i] for i in range(len(self)))
        return NotImplemented
    
    def __rmul__(self, other):
        return self * other
     
        
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord / other for coord in self.coords))
        return NotImplemented

    def __rtruediv__(self):
        return NotImplemented


    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*(coord ** other for coord in self.coords))
        return NotImplemented

    def __rpow__(self):
        return NotImplemented
    

    def __matmul__(self, other) -> int:
        'Computes the cross product of two vectors.'
        if isinstance(other, Vector):
            if len(self) == len(other) == 3:
                a1, a2, a3 = self.coords
                b1, b2, b3 = other.coords
                i = a2 * b3 - a3 * b2
                j = a1 * b3 - a3 * b1
                k = a1 * b2 - a2 * b1
                return Vector(i, -j, k)
            
            elif len(self) == len(other) == 7:
                a1, a2, a3, a4 ,a5, a6, a7 = self.coords
                b1, b2, b3, b4 ,b5, b6, b7 = other.coords
                i = a2 * b4 - a4 * b2 + a3 * b7 - a7 * b3 + a5 * b6 - a6 * b5
                j = a3 * b5 - a5 * b3 + a4 * b1 - a1 * b4 + a6 * b7 - a7 * b6
                k = a4 * b6 - a6 * b4 + a5 * b2 - a2 * b5 + a7 * b1 - a1 * b7
                l = a5 * b7 - a7 * b5 + a6 * b3 - a3 * b6 + a1 * b2 - a2 * b1
                m = a6 * b1 - a1 * b6 + a7 * b4 - a4 * b7 + a2 * b3 - a3 * b2
                n = a7 * b2 - a2 * b7 + a1 * b5 - a5 * b1 + a3 * b4 - a4 * b3
                o = a1 * b3 - a3 * b1 + a2 * b6 - a6 * b2 + a4 * b5 - a5 * b4
                return Vector(i, j, k, l, m, n, o)

            else:
                raise ValueError(
                    f'You can only get a cross product in three and seven dimensional space.'
                )
            

    def __eq__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other) and all(self[i] == other[i] for i in range(len(self))):
                return True
            return False
        return NotImplemented
    
    def __setitem__(self, index, value):
        self.coords[index] = value

    def __getitem__(self, index):
        return self.coords[index]
    

    def __len__(self):
        return len(self.coords)



x = Vector(1, 2, 3)
y = Vector(4, 5, 6)
z = Vector(7, 8, 9)

w = x - y

u7 = Vector(1, 2, 3, 4, 5, 6, 7)
v7 = Vector(3, 4, 5, 6, 7, 8, 9)

print(x)
print(y)
print(z)
print(w)
print(-y) 
print(abs(x))
print(z ** 2)
print(z * 2)
print(2 * z)
print(~z)
print(x * ~x)
print(x * y)
print(x @ x)
print(x @ y)
print(y @ x)
print(u7 @ v7)
print(u7 * v7)
print(y.__doc__)

print(x)
x2 = -(-x)
print(x2)
print(x == x2)
print(x == 1)
print(1 == x)
print(x * x)
print(y * y)
