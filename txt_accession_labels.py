import argparse, sys, os
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser(description="Create labels for your accessions.  Please provide the donor name, within quotes, and the donor number.")
    parser.add_argument("donor", help="The name of person, family, or organiation that donated the accession\nPlease have the donor name within quotation marks.")
    parser.add_argument("number", help="The donor ID number from ArchivesSpace")
    args = parser.parse_args()
    donor = args.donor
    donor_number = args.number
    print("You are making labels for \n" + donor + "\n" + "Donor No. " + donor_number)
    return donor, donor_number

def file_create(labels, donor):
    os.chdir("..") #use this to save the labels to the directory of your choice
    file_name = donor + ".txt"
    label_file = open(file_name, "w")
    label_file.write(labels)
    label_file.close()
    print("The labels have been created! Please open " + file_name + " and print the document! ")

def accession_date():
    yes = ["yes", "Yes", "YES", "Y", "y"]
    yesno = input("Is the date of the accession the current date? (Y/N) ")
    if yesno in yes:
        now = datetime.now()
        accession_date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
    else:
        accession_date = input("What is the date of the accession? Follow the format MM/DD/YYYY ")
    return accession_date

def container_types():
    #user input to note each extent type for the box listing
    yes = ["yes", "Yes", "YES", "Y", "y"]
    containers = {}
    containers["Box"] = int(input("\nHow many boxes are in the accession? "))
    containers["Folder"] = int(input("\nHow many folders are in the accession? "))
    containers["Volume"] = int(input("\nHow many volumes are in the accession? "))
    containers["Roll"] = int(input("\nHow many rolled items are in the accession? "))
    question = input("\nAre there any 'miscellaneous' items in the accession? ")
    if question in yes:
        misc_type = input("\nWhat is the extent type? ")
        containers[misc_type] = int(input("How many " + misc_type + " are found in the accession?"))
    else:
        containers["Item"] = 0
    return containers

def label_maker(donor, number, date, containers):
    labels_list = []
    if containers == {"Box" : 0, "Folder" : 0, "Volume" : 0, "Roll" : 0, "Item": 0}:
        print("No labels have been created.  Goodbye!")
        sys.exit()
    else:
        for k, v in containers.items():
            count = 1
            while count <= v:
                label_line = donor + "\n" + "Donor no. " + number + "\n" + date + "\n" + k + " " + str(count) + " of " + str(v)
                count = count + 1
                labels_list.append(label_line)
        finished_labels = "\n\n\n\n".join(labels_list)
        return finished_labels

try:
    donor, donor_number = get_arguments()
    acc_date = accession_date()
    containers = container_types()
    labels = label_maker(donor, donor_number, acc_date, containers)
    file_create(labels, donor)
except KeyboardInterrupt:
    print("\nGoodbye!")
    sys.exit()
