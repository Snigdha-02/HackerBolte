import Hospital as H
import Doctor as D
import Patient as P



hospital1 = H.Hospital("Manipal Hospital Delhi", "Palam Vihar, Sector 6 Dwarka, Dwarka, New Delhi, Delhi 110075",'ManipalDelhi.txt',4.3,'011 4967 4967')
hospital2 = H.Hospital("Dharamsila Narayan Hospital","Metro Station, Dharamshila marg, Vasundhara Enclave Near Ashok Nagar, Dallupura, New Delhi, Delhi 110096",'Dharamsila.txt',4.3,'080675 06880')

hospital3 = H.Hospital("Bombay Hospital & Research Centre", "12,Vitthaldas Thackersey Marg, New Marine Lines,Mumbai 400020", 'BombayHospi.txt',4.5,'022 2206 7676')

# hospital1.displayDoctors()
# hospital2.displayDoctors()
# hospital3.displayDoctors()

khushi = P.Patient("Khushi Baghel", "11111111", "b20249@students.iitmandi.ac.in", "Palam Vihar, Sector 6 Dwarka, Dwarka, New Delhi, Delhi 110075", "2 March, Evening", "Love with vsVipul")

hopitals = [hospital1,hospital2,hospital3]


def newPatient(name, contact,email,loc,time, query):
    patient = P.Patient(name, contact, email, loc, time, query)

    if query == "Emergency":
        emergency(patient)
    elif query == "Online Consultancy":
        onlineConsult(patient)
    elif query == "Later Appointment":
        forAppointment(patient)




def emergency(patient):
    data = ''
    for hospital in hopitals:
        if patient.getLocation() in hospital.getLocation():
            data += "Hospital -> {}, HelpLine -> {}\n".format(hospital.getName(),hospital.getHelpLine())

    return data


def onlineConsult(patient):
    data = ''
    for hospital in hopitals:
        name,contact,depart,avai = hospital.displayDoctors()
        data += "Hospital -> {}, Doctor -> {}, Contact -> {}, Specialist -> {}, Time - {}\n".format(hospital.getName(),name,contact,depart,avai)

    return data


def makeAppointment(patient,hospi, doctor):   #Clicking on submit button
    hospi.entryPatient(patient,doctor)
    return "Thanks for visiting us!"


def forAppointment(patient):
    data = ''
    for hospital in hopitals:
        name, contact, depart, avai = hospital.displayDoctors()
        if patient.getLocation() in hospital.getLocation():
            data += "Hospital -> {},Location -> {},\n    Doctor -> {}, Contact -> {}, Specialist -> {}, Time - {}\n".format(hospital.getName(),hospital.getLocation(), name, contact, depart, avai)

    return data


print(makeAppointment(khushi,hospital1,"Vipul Sharma"))







