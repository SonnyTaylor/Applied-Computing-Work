# The All-Star Sports Club needs to find out who is eligible to enter an upcoming Masters event.
# All participants in the Masters event must be 40 years old or olden The club needs to print out a list of eligible members.
# When the club's system is running, all data is stored in a series of arrays. The relevant fields are
# date_of_birth[], surname[], firstname[] and gender[], all with the same index value for all fields ofa member.
# The variable numbermembers holds the number of members of the club and the arrays start at the value 1.
# It has been proposed to add a procedure that will start at the first record and look through each record,
# printing out the first name, surname, gender and date of birth of each person who is at least 40 years old.
# To compute age, all members must be born before 1977.


date_of_birth = [1970, 1975, 1980, 1985, 1990]
surname = ["Smith", "Jones", "Taylor", "Brown", "Williams"]
firstname = ["John", "David", "Peter", "Paul", "Simon"]
gender = ["M", "M", "M", "M", "M"]
number_members = len(date_of_birth)

# Iterate through each member
for i in range(1, number_members + 1):
    # Check if the member is born before 1977 and is at least 40 years old
    if date_of_birth[i - 1] < 1977 and 2024 - date_of_birth[i - 1] >= 40:
        # Print the member's information
        print(
            f"First Name: {firstname[i - 1]}, Surname: {surname[i - 1]}, Gender: {gender[i - 1]}, Date of Birth: {date_of_birth[i - 1]}"
        )
