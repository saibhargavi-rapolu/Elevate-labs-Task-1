import pandas as pd

d = pd.read_csv("C:/Users/bharg/OneDrive/Documents/medical_appointment_no_shows.csv")

print("identifying missing_values")
missing_values = d.isnull().sum()
print(missing_values)


print("\n\nidentifying duplicates")
print(d.duplicated().sum())

print(d['PatientId'].duplicated().sum() )
print(d[['PatientId','No-show']].duplicated().sum())
d.drop_duplicates(['PatientId','No-show'],inplace=True)
print(d)
print("\n\nAfter : ",d[['PatientId','No-show']].duplicated().sum())

print("\n\nstandardizing text values")
print(d['Gender'],d['Neighbourhood'])
d['Gender'] = d['Gender'].str.upper().str.strip()
d['Neighbourhood'] = d['Neighbourhood'].str.title()
print("\n\nAfter : \n",d['Gender'],d['Neighbourhood'])

print("\n\nconvert date formats")
d['ScheduledDay'] = pd.to_datetime(d['ScheduledDay'])
d['AppointmentDay'] = pd.to_datetime(d['AppointmentDay'])
print(d['ScheduledDay'],d['AppointmentDay'])

print("\n\nrename column headers")
d.columns = [col.lower().replace('-', '_') for col in d.columns]
print(d)


print("\n\nfix data types")
d['age'] = d['age'].astype(int)
print(d['age'])

