
import pandas as pd
import os

election_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

election_data = pd.read_csv(election_csv)

election_data.info()

total_votes = len(election_data)

candidate_list = election_data['Candidate'].unique()

vote_counts = election_data['Candidate'].value_counts()


vote_percentage = vote_counts / total_votes*100


print('Election Results')
print('----------------------------')
print ("Total Votes: %d" % total_votes) #d=int
print('----------------------------')
for i in range(len(vote_counts)):
    print("%s: %6.3f%% (%d)" % (candidate_list[i], vote_percentage[i], vote_counts[i]))
print('----------------------------')
print("Winner: %s" % candidate_list[0])
print('----------------------------')





