import random 
def game_win(user,computer):
    if(user==computer):
        return None
    if(user=="s" and computer=="p"):
        return False
    if(user=="s" and computer=="sc"):
        return True 
    if(user=="p" and computer=="s"):
        return True
    if(user=="p" and computer=="sc"):
        return False
    if(user=="sc" and computer=="s"):
        return False
    if(user=="sc" and computer=="p"):
        return True
rand_no=random.randint(1,3)
print("Computer's Turn\n")
if(rand_no==1):
    computer="s"
elif(rand_no==2):
    computer="p"
else:
    computer="sc"
user=input("User's Turn\n").lower()
print(f"computer choose {computer}")
result=game_win(user,computer)
if result is None:
    print("It's a draw")
elif(result):
    print("You win")
else:
    print("You lose ")




