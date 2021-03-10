import time
from random import randint
print("You're about to vote for your future president")
time.sleep(2)
print("The aspirant are 'JOSEPH' & 'Chinedu'")
print()
nominee1v= 0
nominee2v = 0

voters_id = [1,2,3]
numf = len(voters_id)
selected_voter_id = [randint(1,10)]


nu_of_voters = len(voters_id)

while True:
    if voters_id == []:
        print("Voting session has ended")
        
        if nominee1v > nominee2v:
            
            perc = (nominee1v / numf)* 100 
            print(f"Joseph have won with {perc}% vote")
            break
        elif nominee2v > nominee1v:
            perc = (nominee2v / numf)* 100 
            print(f"Chinedu have won with {perc * 100}% vote")
            break
    else:
        print(f"Here's all the voters id. {voters_id}. ")
        voter = int(input("Enter your vote id: "))   
        if voter in voters_id:
            
            # selected_voter_id.remove(voter)
            vote = input("Enter your vote, 'J' OR 'C'~: ").casefold()
            if vote == 'j':
                nominee1v += 1
                print("Your vote for JOSEPH have been recorded. Thank you for your vote")
                voters_id.remove(voter)
            elif vote == 'c':
                nominee2v += 1
                print("Your vote for Chinedu have been recorded. Thank you for your vote")
                voters_id.remove(voter)
            else:
                print("he's not a president aspirant")
                continue
        else:
            print("You're not a voter here or you've already voted!")