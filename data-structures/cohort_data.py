"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    
    houses = set()
    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        if len(words[2]) > 1 :
            houses.add(words[2])
        
    return houses


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """ 

    students = []
    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        firstname = words[0]
        lastname = words[1]
        if words[4] == "G" or words[4] == "I":
            continue

        if cohort == "All":
            students.append(f"{firstname} {lastname}")
        elif cohort == words[4]:
            students.append(f"{firstname} {lastname}")

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        firstname = words[0]
        lastname = words[1]
        if words[4] == "G":
            ghosts.append(f"{firstname} {lastname}")
        elif words[4] == "I":
            instructors.append(f"{firstname} {lastname}")
        elif words[2] == "Dumbledore's Army":
            dumbledores_army.append(f"{firstname} {lastname}")
        elif words[2] == "Gryffindor":
            gryffindor.append(f"{firstname} {lastname}")
        elif words[2] == "Hufflepuff":
            hufflepuff.append(f"{firstname} {lastname}")
        elif words[2] == "Ravenclaw":
            ravenclaw.append(f"{firstname} {lastname}")
        elif words[2] == "Slytherin":
            slytherin.append(f"{firstname} {lastname}")

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        full_name = words[0] + " " + words[1]
        house = words[2]
        advisor = words[3]
        cohort = words[4]

        student_info_list = [full_name, house, advisor, cohort]

        tuple_list = tuple(student_info_list)
        all_data.append(tuple_list)


    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        full_name = words[0] + " " + words[1]
        if full_name == name:
            return words[4]

    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    duplicated_lastname = set()
    list_lastname = [];
    data = open(filename)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        last_name = words[1]
        if last_name not in list_lastname:
            list_lastname.append(last_name)
        else:
            duplicated_lastname.add(last_name)

    # return list_lastname
    return duplicated_lastname

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set()

    data = open(filename).readlines()
    # print(data)

    for line in data:
        line = line.rstrip()
        words = line.split("|")
        firstname = words[0]
        lastname = words[1]
        full_name = words[0] + " " + words[1]
        if full_name == name:
            student_house = words[2]
            student_cohort = words[4]
            # print(student_house, student_cohort)
            break


    for line in data:
        line = line.rstrip()
        words = line.split("|")
        full_name = words[0] + " " + words[1]
        if words[2] == student_house and words[4] == student_cohort and full_name != name:
            housemates.add(full_name)

    return housemates




##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
