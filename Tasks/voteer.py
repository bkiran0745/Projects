import hashlib

class Voter:
    def __init__(self, name, voter_id):
        self.name = name
        self.voter_id = voter_id
        self.voted = False

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

class VotingSystem:
    def __init__(self):
        self.voters = []
        self.candidates = []

    def register_voter(self, name):
        voter_id = hashlib.sha256(name.encode()).hexdigest()
        new_voter = Voter(name, voter_id)
        self.voters.append(new_voter)
        return new_voter

    def register_candidate(self, name):
        new_candidate = Candidate(name)
        self.candidates.append(new_candidate)
        return new_candidate

    def display_candidates(self):
        print("Candidates:")
        for idx, candidate in enumerate(self.candidates, 1):
            print(f"{idx}. {candidate.name}")

    def vote(self, voter, candidate_index):
        if not voter.voted and 1 <= candidate_index <= len(self.candidates):
            candidate = self.candidates[candidate_index - 1]
            candidate.votes += 1
            voter.voted = True
            print(f"Thank you, {voter.name}, for voting for {candidate.name}!")

        elif voter.voted:
            print("You have already voted!")

        else:
            print("Invalid candidate index. Please choose a valid candidate.")

# Example usage:

voting_system = VotingSystem()

# Register voters
num_voters = int(input("Enter the number of voters: "))
for _ in range(num_voters):
    voter_name = input("Enter voter name: ")
    voting_system.register_voter(voter_name)

# Register candidates
num_candidates = int(input("Enter the number of candidates: "))
for _ in range(num_candidates):
    candidate_name = input("Enter candidate name: ")
    voting_system.register_candidate(candidate_name)

# Display candidates
voting_system.display_candidates()

# Voters cast their votes
for voter in voting_system.voters:
    if not voter.voted:
        print(f"\n{voter.name}, it's time to vote!")
        voting_system.display_candidates()
        candidate_index = int(input("Enter the index of the candidate you want to vote for: "))
        voting_system.vote(voter, candidate_index)

# Display results
print("\nElection Results:")
for candidate in voting_system.candidates:
    print(f"{candidate.name}: {candidate.votes} votes")
