# Obtener solo las permutaciones distintas
class perm_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset = set(elements)
    listunique = [perm_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return u_perm_ctor(listunique, [0]*u, u-1)

def u_perm_ctor(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in  u_perm_ctor(listunique, result_list, d-1):
                    yield g
                i.occurrences += 1

# Obtener todas las permutaciones
def all_perms(start, end=[]):
    if(len(start) == 0):
        print(end)
    else:
        for i in range(len(start)):
            all_perms(start[:i] + start[i+1:], end + start[i:i+1])
            
# Prueba
set_ejemplo = [1, 1, 2, 2]
unique = list(perm_unique(set_ejemplo))

print("Set base: ", set_ejemplo)
print("\nPermutaciones distintas:\n")
print(unique)
print("\nTodas las permutaciones:\n")
all_perms(set_ejemplo)