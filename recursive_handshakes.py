#In a party of N people, each person will shake her/his hand with each other person only once. 
#In total how many hand-shakes would happen?
 
#n = int(input("How many people have to shake hands?\n"))
#print(f"{n} people have to shake hands.")

def recursive_hand_shakes(n):
    if n == 0:
        return 0
    else:
        return n-1 + recursive_hand_shakes(n - 1)



#only the men will shake hands with everyone else:
def recursive_handshakes_couples(n):
    global x
    if n <= x/2:
        return 0
    else:
        return (n-2) + recursive_handshakes_couples(n-1)
        

couples = int(input("How many couples have to shake hands?\n"))
# since they are couples, x will always be an even number
x=couples*2
result = recursive_handshakes_couples(x)
print(f"total handshakes = {result}")