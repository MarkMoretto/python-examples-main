

"""
Topic: Create a small grade handler script with ability to add/remove classes and display classes with grades
Date created: 2019-03-09
Contributor(s): Mark Moretto

https://stackoverflow.com/questions/55077190/creating-a-subject-and-grading-system-in-python
"""




__name__ = 'DEMO'

class GradeHandler(object):

    EMNER = ["INFO100","INFO104","INFO110","INFO150","INFO125"]
    FAGKODER= [["Informasjonsvitenskap","INF"],["Kognitiv vitenskap","KVT"]]
    KARAKTERER = [["INFO100","C"],["INFO104","B"],["INFO110","E"]]

    def __init__(self):
        self.Emner = self.EMNER
        self.FagKoder = self.FAGKODER
        self.Karakterer = self.KARAKTERER
        self.__create_grade_dict()



    def remove_subject(self, subject_name):
        """
        Remove a subject ot the classes class list variable.
        """
        try:
            self.Emner = [i for i in self.EMNER if i != subject_name]
            self.__create_grade_dict()
        except ValueError:
            pass


    def add_subject(self, subject_name):
        """
        Append a subject ot the classes class list variable.
        """
        if not subject_name in Emner:
            self.Emner.append(subject_name)
            self.__create_grade_dict()



    def __create_grade_dict(self, grade_dict=None):
        """
        Split grades matrix into separate parts; Create and set a dictionary of values.
        """
        if grade_dict is None:
            self.grade_dict = dict()
    
        sub, grade = zip(*self.Karakterer)
        karakterer_dict = {k:v for k, v in list(zip(sub, grade))}
    
        for i in self.Emner:
            if i in karakterer_dict.keys():
                self.grade_dict[i] = karakterer_dict[i]
            else:
                self.grade_dict[i] = ''



    def update_grade(self, subject_name, grade='A'):
        """
        Update a grade in the grade dictionary.
        Will also add a subject if not alrady in the dictionary.
        """
        try:
            self.grade_dict[subject_name] = grade
        except (KeyError, ValueError):
            pass




    def print_grades(self, subject_name=None):
        """
        Print dictionary results.
        """
        if subject_name is None:
            for k, v in self.grade_dict.items():
                print('{} {}'.format(k, v))

        else:
            if subject_name in self.grade_dict.keys():
                print('{} {}'.format(subject_name, self.grade_dict[subject_name]))




if __name__ == 'DEMO':

    ### Create an instance of the GradeHandler and print initial grades.
    gh = GradeHandler()
    gh.print_grades()


    ### Append a class
    gh.add_subject('GE0124')
    gh.print_grades()


    ### Add grade 
    gh.update_grade('GE0124', 'B+')
    gh.print_grades()


    ### Update grades
    gh.update_grade('GE0124', 'A-')
    gh.print_grades()


    ### Remove subject (will also remove grade.
    gh.remove_subject('GE0124')
    gh.print_grades()



### Original stuff below.  Went with class instead.

#def add_subject(subject_name):
#    if not subject_name in Emner:
#        Emner.append(subject_name)
#        return Emner
#    else:
#        return Emner


#Emner = add_subject('INFO100') # Won't add duplicate
#Emner = add_subject('GE0124') # Adds new subject


#def remove_subject(subject_name):
#    try:
#        Emner.remove(subject_name)
#    except ValueError:
#        pass
#    return Emner


#Emner = remove_subject('GE0124') # Will remove just-added subject.



#def process_grades():
    
#    grade_dict = dict()

#    sub, grade = zip(*Karakterer)
#    karakterer_dict = {k:v for k, v in list(zip(sub, grade))}
    
#    for i in Emner:
#        if i in karakterer_dict.keys():
#            grade_dict[i] = karakterer_dict[i]
#        else:
#            grade_dict[i] = ''

#    return grade_dict


#def print_grades():
#    """
#    Print dictionary results.
#    """
#    ddict = display_grades()
#    for k, v in ddict.items():
#        print('{} {}'.format(k, v))


#print_grades() # Print all grades