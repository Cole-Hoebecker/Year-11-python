pet_name = ["Foxy", "Kevin", "Sally"]
species = ["Dog", "Rat", "Lemur"]
age = [8, 3, 9]
vaccination_status = [True, False, True]

pet_name.append("Hootie")
species.append("Blowfish")
age.append(34)
vaccination_status.append(True)

index = pet_name.index("Foxy")
pet_name.remove("Foxy")
species.remove(species[index])
age.remove(age[index])
vaccination_status.remove(vaccination_status[index])



for i in range(len(pet_name)):
    print("Pet name:", pet_name[i])
    print("Species:", species[i])
    print("Age:", age[i])
    if vaccination_status[i] == False:
        vaccination_status[i]S = True
    print("Vaccination_status:", vaccination_status[i])
    print()