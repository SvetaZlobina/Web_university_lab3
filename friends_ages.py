from client_friends import ClientFriends
from client_id_from_username import ClientIdFromUsername
#import matplotlib.pyplot as pyplot

client_by_username = ClientIdFromUsername('pakahontas')
client_by_username.execute()
print(client_by_username.real_id)

client = ClientFriends(client_by_username.real_id)
client.execute()
print(client.ages_list)

ages_dict = [0] * 120
for age in client.ages_list:
    ages_dict[age] += 1

for number in range(110):
    if ages_dict[number] > 0:
        print(number, ': ', '#'*ages_dict[number])

# pyplot.hist(client.ages_list, client.ages_list.len)