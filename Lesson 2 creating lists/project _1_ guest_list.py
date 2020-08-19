guest_list = "person one", "person two", "person three"
guest_invite = "Hello, " + guest_list[0].title() + " you are invited to dinner next Monday."
print(guest_invite)

guest_invite = "Hello, " + guest_list[1].title() + " you are invited to dinner next Monday."
print("\n" + guest_invite)

guest_invite = "Hello, " + guest_list[2].title() + " you are invited to dinner next Monday."
print("\n" + guest_invite)

# person two cannot come, invite person two.one

guest_list.remove("person one")
