# write a voting system in python

import operator
import collections

def check_vote(votes):
    valid_votes = ["a", "b", "c"]
    for vote in votes:
        if vote not in valid_votes:
            print("Invalid vote found: ", vote)
            return False
    return True

def vote(candidate, votes):
    if not check_vote(votes):
        return
    count = collections.Counter(votes)
    sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    print("\nVote count for candidate", candidate)
    for i in sorted_count:
        print(i[0], " - ", i[1])

    print("\nThe winner is: ", sorted_count[0][0])

candidate = input("Enter the candidate name: ").lower()
votes = input("Enter the votes, separated by space: ").lower().split()
vote(candidate, votes)