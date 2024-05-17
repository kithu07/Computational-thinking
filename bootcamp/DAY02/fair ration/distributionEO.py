def is_even ( n: "int" ) -> int :
    return n % 2 == 0
def encode (
def check_condition ( queue : "list[int]" ) -> str :
    if not is_even ( sum(queue) ):
        return "NO"
    return str(distribute(queue))
def distribute ( queue : "list[int]" ) -> int:
    if len(queue) == 1:
        return 0
    elif is_even( queue[0] ) :
        return distribute(queue[1:])
    else:
        return 2 + distribute( [queue[1] + 1] + queue[2:] )
    
print(check_condition( [2, 3, 4, 5, 6] ))
