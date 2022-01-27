#3-1 
friend_names = ["Luke", "Mike", "Devin"]
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])

#3-2
print(f"\nHello, {friend_names[0]}")
print(f"Hello, {friend_names[1]}")
print(f"Hello, {friend_names[2]}")

#3-3
transportation = ["Vespa", "Boat"]
print(f"\nI would like to own a {transportation[0]} someday.")
print(f"It sounds like a lot of work to own a {transportation[1]}.")

#3-4
guest_list = ["Dostoyevsky", "Rivers Cuomo", "J. D. Sallinger"]
print(f"\nI formally invite you to dinner, Mr. {guest_list[0]}.")
print(f"Let\'s hang out, {guest_list[1]}")
print(f"Shoutout to {guest_list[2]}")

#3-5
#JD Sallinger couldn't make it
guest_list[2] = "David Foster Wallace"
print(f"Dear {guest_list[2]}, you have been invited to dinner.")

#3-6
#add more guests
guest_list.insert(0, "Anime Jones")
guest_list.insert(2, "Anime Johnson")
guest_list.append("Anime Johnston")
print(f"\nCome to dinner, {guest_list[0]}")
print(f"Come to dinner, {guest_list[2]}")
print(f"Come to dinner, {guest_list[-1]}")

#3-7
#remove guests so there are only 2
#use the pop method
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(f"\nYou have formally been invited to dinner, {guest_list[0]}")
print(f"You have formally been invited to dinner, Mr. {guest_list[1]}")

#3-8
places = ["Japan", "Ireland", "Germany", "South Korea", "Tibet"]
#original order
print(places)
#use sorted to temporarily sort it
print(sorted(places))
#prove the original list is still in its original order
print(places)
#reverse the list order
places.reverse()
#note: if you try print(places.reverse()) it will give None
    #this is because the list change should happen before printing
print(places)
#reverse the list back to normal
places.reverse()
print(places)
#use sort() on the list
places.sort()
print(places)
#sort() again to reverse it, using .sort(reverse=True)
places.sort(reverse=True)
print(places)

#3-9
guest_length = str(len(guest_list))
print(f"\nThere are {guest_length} guests coming to dinner.")
