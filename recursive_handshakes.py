#In a party of N people, each person will shake her/his hand with each other person only once. 
#In total how many hand-shakes would happen?
 
n = int(input("How many people have to shake hands?\n"))
print(f"{n} people have to shake hands.")

def recursive_hand_shakes(n):
    if n == 0:
        return 0
    else:
        a = n-1
        print(f"Person {n} shakes hand with {a} other persons")
        return n-1 + recursive_hand_shakes(n - 1)
        
result = recursive_hand_shakes(n)
print(result)