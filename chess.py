def all_knight_moves(n):
    def moves(x, y):
        return [
            (x+1, y+2), 
            (x+1, y-2), 
            (x-1, y+2), 
            (x-1, y-2), 
            (x+2, y+1), 
            (x+2, y-1), 
            (x-2, y+1), 
            (x-2, y-1)
        ]
    def in_bounds(x, y):
        return x >= 0 and x < n and y >= 0 and y < n
    def next_moves(x, y, seen):
        m = moves(x, y)
        return [ (x2, y2) for (x2, y2) in m if in_bounds(x2, y2) and (x2, y2) not in seen ]
    def knight_moves(x, y, seen):
        if (x, y) in seen:
            return []
        seen.add((x, y))
        return [ (x, y) ] + sum([ knight_moves(x2, y2, seen) for (x2, y2) in next_moves(x, y, seen) ], [])
    return [ knight_moves(x, y, set()) for x in range(n) for y in range(n) ]

def get_first_path(n):
    return all_knight_moves(n)[0]

size = 3
print("\nCamino partiendo desde la casilla (0, 0) en un tablero 3x3:\n")
print(get_first_path(size))
print("\n")
print("Todos los caminos posibles:\n")
print(all_knight_moves(size))