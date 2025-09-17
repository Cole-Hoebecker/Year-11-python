name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

#check if credit card is verified based on length of card and its format
def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False

def vaccinate():
  vaccinated == True

verify_credit_card('1234 4334 1001 0000')
help()
#Verifying credit card number. If verified, pay 39 dollars and vaccinate the pet
clientccardnumber = input("Please enter your credit car number: ")
if verify_credit_card(clientccardnumber) == True:
  print("Your card has been accepted")
  account_balance -= 39
  vaccinate()

increase_age()
print('age:', age)
