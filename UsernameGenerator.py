from xml.dom import UserDataHandler
from datetime import date
import sys

def user_details():
    """
    Prompt user input
    """
    while True:
        first_name = input("Insert your first name")
        if first_name.isalpha():#check if the user entered alphabetic letters only
            while True:#verify if the first name is more than 2 letters if not add "O" at the end
                if len(first_name) == 2:
                    first_name = first_name + str("o")
                elif len(first_name) == 1:
                    first_name = first_name + str("oo")
                    break
                break
        else:#if first_name not characters print statement below and exit
            print("Please enter alphabetic characters and no spacing!")
            first_name = input("Please enter your first name: ")
        last_name = input("Insert your last name")
        if last_name.isalpha():#check to confirm if user input is alphabetic letters plus no spacing
            while True:
                if len(last_name) == 2:
                    last_name = last_name + str("o")
                elif len(last_name) ==1:
                    last_name = last_name + str("oo")
                    break
                break
        else:
            last_name = str(input("Enter your last name: "))
        cohort = str(input("Enter your Cohort Year: "))
        if cohort.isdigit():#confirm if the cohort year is digits
            while True:
                if cohort == str(date.today().year):#verify that cohort year is the current year
                    break
                else:
                    print("An error was encountered with the given cohort year!")
                    user_details()
                break
        else:
            print("Please enter a valid cohort year in digits only!")
            user_details()
        campus = str(input("Please enter your campus: ").upper())
        if campus.isalpha():
            while True:
                user_campus(campus)
                if 'durban' in campus:
                    return campus
                elif 'cape town' in campus:
                    return campus
                elif 'johannesburg' in campus:
                    return campus
                elif 'phokeng' in campus:
                    return campus
                break
        else:
            break
        break

    create_user_name(first_name, last_name, cohort,campus)
    print("First Name: ",first_name,"\nLast Name: ",last_name,"\nCohort Year: ",cohort, "\nFinal Campus: ", campus, "\nFinal username: ", create_user_name(first_name, last_name, cohort, campus))

    """Ask the user if final username is correct
    Let the user know what the format of the username is
    and if the final username is correct
    """
    print((first_name[-3:]).lower(),"-Last 3 letters of the First Name")
    print((last_name[0:3]).lower(), "-First 3 letters of the Last Name")
    print(campus.upper(), "-Final Campus selection, DBN for Durban, JHB for Johannesburg, CPT for Cape Town, PHO for Phokeng")
    print(cohort, "-The cohort year is the current bootcamp year")
    ans = str(input("Is the Username correct?\nY/N: ").lower().strip())
    def ans_yes(ans):
        if "yes" or "y" in ans:
            print("Username Confirmed!")
    def ans_no(ans):
        if "no" or "n" in ans:
            print("Okay enter your desired username: ")
            pass
    if ans =='y':
        ans_yes(ans)
        pass
    elif ans =='n':
        ans_no(ans)
        pass
def create_user_name(first_name, last_name, cohort, campus):
    """
    Create and return a valid username
    """
    user_campus(campus)
    username = (first_name[-3:] + last_name[0:3]).lower() + campus + cohort
    return username

def user_campus(campus):
    """
    Return Valid campus abbreviations
    """
    campus_dictionary = {"johannesburg": "JHB",
                         "durban": "DBN",
                         "cape town": "CPT",
                         "phokeng": "PHO"}
    def dbn_camp(campus):
        if 'durban' in campus:
            campus = campus_dictionary["durban"]
        return  campus
    def cpt_camp(campus):
        if 'cape town' in campus:
            campus = campus_dictionary["cape Town"]
        return campus
    def jhb_camp(campus):
        if 'johannesburg' in campus:
            campus = campus_dictionary["johannesburg"]
        return campus
    def pho_camp(campus):
        if 'phokeng' in campus:
            campus = campus_dictionary["phokeng"]
        return campus
    if 'durban' in campus:
        dbn_camp(campus)
    elif 'cape town' in campus:
        cpt_camp(campus)
    elif 'johannesburg' in campus:
        jhb_camp(campus)
    elif 'phokeng' in campus:
        pho_camp(campus)

if __name__ == '__main__':
    user_details()

    
