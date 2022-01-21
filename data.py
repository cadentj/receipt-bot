def get_colleges_dic() :
    college_list = {
        "Case Western" : "admission@case.edu",
        "University of Chicago" : "collegeadmissions@uchicago.edu",
        "Tulane" : "undergrad.admission@tulane.edu",
        "Yale" : "donotreply@yale.edu",
        "Brandeis" : "admissions@brandeis.edu",
        "Carnegie Mellon" : "admission@andrew.cmu.edu"
    }
    return college_list

def get_colleges() :
    return get_colleges_dic().keys()

def create_email_list(college_names) :
    college_list = get_colleges()
    email_list = []
    for college in college_names :
        email_list.append(college_list[college])

    print(email_list)
    return email_list