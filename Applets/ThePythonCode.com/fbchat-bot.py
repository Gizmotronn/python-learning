from fbchat import Client
from fbchat.models import Message

# From https://www.thepythoncode.com/article/make-bot-fbchat-python

# Facebook user credentials - i'll set up a test account
username = "allianceofdroidsla@gmail.com"
password = "aodroids"

# Login
client = Client(username, password)


# Get 20 users I most recently contacted - dir()
users = client.fetchThreadList()
print(users) # results in a list of threads - // these can be users or groups

# Get detailed information about these users
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]

# Sorting messages by number of messages between you and the thread // to detect best friend (or at least most contacted one) // we can sort by this attribute
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
# Print the best friend!
best_friend = sorted_detailed_users[0]
print("Best friend: ", best_friend.name, " with a message count of ", best_friend.message_count)

# Congratulate the best friend by sending a message: 
client.send(Message(text=f"Congratulations {best_friend.name}, you are my best friend on Facebook with {best_friend.message_count} messages! This is a python script that I coded myself to detect the users that I message the most and send them a message! This is me testing for a chatbot I'm making for a client, this will not be repetitive and my code will not spam you. Good day, king "), thread_id=best_friend.uid)

# Let's logout!
client.logout()