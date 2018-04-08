## Lauro Cabral
## April 9,2018

## Task 2.12.1
def create_voting_dict(strlist):
    outdict = {}
    for line in strlist:
        senator = line.split()
        outdict[senator[0]] = list(int(i) for i in senator[3:len(senator)])

    return outdict


myList = list(open('voting_record_dump109.txt'))
votingDict = create_voting_dict(myList)


## Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    return sum([ a*b for (a,b) in zip(voting_dict[sen_a], voting_dict[sen_b]) ])

print(policy_compare('Akaka','Alexander',votingDict))

## Task 2.12.3
def most_similar(sen, voting_dict):
    distance = { k:policy_compare(sen, k, voting_dict) for k in voting_dict if k != sen }
    v=list(distance.values())
    k=list(distance.keys())
    return k[v.index(max(v))]

print(most_similar('Akaka',votingDict))

## Task 2.12.4
def least_similar(sen, voting_dict):
    distance = { k:policy_compare(sen, k, voting_dict) for k in voting_dict if k != sen }
    v=list(distance.values())
    k=list(distance.keys())
    return k[v.index(min(v))]

print(least_similar('Akaka',votingDict))


## Task 2.12.5
print('Most Like Chafee: ' + str(most_similar('Chafee',votingDict)))
print('Least Like Santorum: ' + str(least_similar('Santorum',votingDict)))

## Task 2.12.6
print('CA & AZ : ' + str(policy_compare('Boxer','Pryor',votingDict)))








