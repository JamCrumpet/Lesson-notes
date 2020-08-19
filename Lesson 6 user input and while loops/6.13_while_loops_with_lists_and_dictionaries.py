# a for loo os effect for looping through a list but you should modify a list within a for loop ...
# ... but you shouldn't modify a list inside a for loop because Python will have trouble keeping track of the list
# to modify a list as you work though it use a while loop
# using a while loop with lists and dictionaries allows you to collect, store and organise lots of inputs

# MOVING ITEMS FROM ONE LIST TO ANOTHER

# consider a list of newly registered users but unverified users on a website
# after verifying these users how can we move them from one list to another, but using a while loop

unconfirmed_users = ["alice", "brian", "candice", "jeff"] # confirm users and move them to confirmed list
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # while loop runs a long as unconfirmed list is not empty ...
    # ... within the loop .pop removes unverified users one at a time from the end of unconfirmed_users

    print("Verifying user: " +current_user.title()) # because jeff is the last person on unconfirmed_users ...
    confirmed_users.append(current_user) # ...  his name will be the first to be removed and stored and ...
    # ... moved to he confirmed users list. candace is next, followed by brian, then alice

# displays all confirmed users
print("\n The following users have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())