
salutation_name = '[name]'

#Create  a list of invitees
with open("./input/Names/List_of_invitees.txt") as invitees:
  list_of_invitees = invitees.readlines()
  
with open("./input/Letters/starting_letter.txt") as letter:
  starting_letter = letter.read()
  for name in list_of_invitees:
    # remove the new lines from the list of invitees
    invited_guest = name.strip()  
    completed_letter = starting_letter.replace(salutation_name, invited_guest)
    #create each letter of invite
    with open(f"./output/completed_letters/letter-for-{invited_guest}", "w") as file:
      file.write(completed_letter)

