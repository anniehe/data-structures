def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """

    houses = set()

    cohort_data = open(filename)

    for line in cohort_data:
        record = line.rstrip()
        data = record.split("|")

        house = data[2]
        if house:
            houses.add(house)

    cohort_data.close()

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    cohort_data = open(filename)

    for line in cohort_data:
        record = line.rstrip()
        data = record.split("|")

        name = data[0] + " " + data[1]
        cohort = data[4]

        if cohort == "Winter 2015":
            winter_15.append(name)

        elif cohort == "Spring 2015":
            spring_15.append(name)

        elif cohort == "Summer 2015":
            summer_15.append(name)

        elif cohort == "TA":
            tas.append(name)

    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()

    all_students.extend([winter_15, spring_15, summer_15, tas])

    cohort_data.close()

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    cohort_data = open(filename)

    for line in cohort_data:
        record = line.rstrip()
        data = record.split("|")

        last_name = data[1]
        house = data[2]
        cohort = data[4]

        if house:

            if house == "Gryffindor":
                gryffindor.append(last_name)

            elif house == "Hufflepuff":
                hufflepuff.append(last_name)

            elif house == "Slytherin":
                slytherin.append(last_name)

            elif house == "Dumbledore's Army":
                dumbledores_army.append(last_name)

            elif house == "Order of the Phoenix":
                order_of_the_phoenix.append(last_name)

            elif house == "Ravenclaw":
                ravenclaw.append(last_name)

        elif cohort == "TA":
            tas.append(last_name)

        else:
            instructors.append(last_name)

    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    ravenclaw.sort()
    tas.sort()
    instructors.sort()

    all_students.extend([hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors])

    cohort_data.close()

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    cohort_data = open(filename)

    for line in cohort_data:
        record = line.rstrip()
        data = record.split("|")

        first_name, last_name, house, advisor, cohort = data
        full_name = first_name + " " + last_name

        if house:
            student_data = (full_name, house, advisor, cohort)
            student_list.append(student_data)

    cohort_data.close()

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    input_name = raw_input("Who are you looking for? ")

    for student_tuple in student_list:
        full_name, house, advisor, cohort = student_tuple

        if input_name == full_name:
            print "%s was found in the %s cohort" % (full_name, cohort)
            return

    print "%s was not found. Perhaps they are staff." % (input_name)

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    # duplicate_names = set()
    winter_15 = set()
    spring_15 = set()
    summer_15 = set()

    cohort_data = open(filename)

    for line in cohort_data:
        record = line.rstrip()
        data = record.split("|")

        first_name, last_name, house, advisor, cohort = data

        if cohort == "Winter 2015":
            winter_15.add(first_name)

        elif cohort == "Spring 2015":
            spring_15.add(first_name)

        elif cohort == "Summer 2015":
            summer_15.add(first_name)

    duplicate_names = winter_15 & spring_15 & summer_15

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
