from os import system, name
from colors import Colors as colors
import time,sys
import random

def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

def typing(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def wait():
  input("Press Enter To Return To Main Screen")
  clear()

typing("Hello And Welcome To Idle Factory!\n\n")
typing("Press [s] To Skip Intro! Else Press [i] For Intro!\n")

skip = input("Skip? ")

while (skip.upper() != ("S") and skip.upper() != ("I")):
  typing("Invalid Response!\n")
  typing("Please Try Again!\n\n")
  skip = input("Skip? ")
  skip.upper()


days = 1
money = 1000
salarypaid =0 
salarycap = 50000
salaryCredits =1  
factoryLevel = 1
machineryLevel =1 
profitLevel =1 
multiplierLevel = 1
factoryCostInc = 1
machineCostInc = 1
profitCostInc = 1
multiplierCostInc = 1

randomquote = [
  '''"The Best Businesses Are The Creative Ones" - Jeff Bezos 2000''',
  '''"Noice" - Noice 2021''',
  '''"Prove Me Wrong: Money = Life" - A Random Guy With Some Common Sense''',
  '''"Invest, Invest, Invest" - Warren Buffet 2015''',
  '''"Run For President" - President''',
  '''"When Life Gives You Lemons, Sell Them And Make Money *duh*" - Bill Gates 2013''',
  '''"Upvote This Game On Repl To Strike It Rich!!" - Very Intelligent Person 2021'''
]

free_agents_first_name_workers = [
  "Molly",
  "John",
  "Jack",
  "Abby",
  "Spence",
  "Liam",
  "Adam",
  "Sophia"
]

free_agents_last_name_workers = [
  "Smith",
  "Johnson",
  "Williams",
  "Brown",
  "Jones",
  "Davis",
  "Taylor",
  "White"
]

prob_free_agents_workers = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

worker_condition = ["Good", "Fair", "Bad"]

free_agents_hired = []
free_agents_hired_salary = []
free_agents_hired_condition = []

def intro():
  typing("One Day While Walking Down An Abandoned Street\n")
  time.sleep(0.5)
  typing("You See An Abandoned Building\n")
  time.sleep(0.5)
  typing("You Have Always Dreamed Of Owning A Business\n")
  time.sleep(0.5)
  typing("So You Buy The Place For $50,000\n")
  time.sleep(0.5)
  typing("This Purchase Places You Near Bankruptcy\n")
  time.sleep(0.5)
  typing("It's A Leap Of Faith, But You Can Do It!\n")
  time.sleep(0.5)
  typing("Let's Begin!!\n\n")
  time.sleep(0.5)

def start():
  print(f"Days: {days}")
  print(f"{colors.bright_green}Money: ${round(money)}{colors.ENDC}")
  if (salarypaid < salarycap/2):
    print(f"Salary: {colors.bright_green}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  elif (salarycap/2 <= salarypaid <= salarycap*(3/4)):
    print(f"Salary: {colors.bright_yellow}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  elif (salarypaid > salarycap*(3/4)):
    print(f"Salary: {colors.red}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  print("Enter The Number To Do The Following: ")
  print("1 : NEXT DAY")
  print("2 : UPGRADE FACTORY")
  print("3 : HIRE STAFF")
  print("4 : FACTORY STATS")
  print("5 : RANDOM QUOTE")
  print("6 : HELP")
  global startChoice
  startChoice = input("")

def upgrade():
  global factoryLevel
  global machineryLevel
  global profitLevel
  global multiplierLevel
  global money
  global salaryCredits
  global salarycap
  global factoryCostInc
  global machineCostInc
  global profitCostInc
  global multiplierCostInc
  print(f"{colors.bright_green}Money: ${round(money)}{colors.ENDC}")
  if (salarypaid < salarycap/2):
    print(f"Salary: {colors.bright_green}${salarypaid}{colors.ENDC} Out Of ${salarycap}")
  elif (salarycap/2 <= salarypaid <= salarycap*(3/4)):
    print(f"Salary: {colors.bright_yellow}${salarypaid}{colors.ENDC} Out Of ${salarycap}")
  elif (salarypaid > salarycap*(3/4)):
    print(f"Salary: {colors.red}${salarypaid}{colors.ENDC} Out Of ${salarycap}")
  print(f"{colors.bright_red}Salary Credits: {salaryCredits}{colors.ENDC}\n")
  print(f"{colors.green}Factory Level: {factoryLevel}{colors.ENDC}")
  print(f"{colors.bright_yellow}Machinery Level: {machineryLevel}{colors.ENDC}")
  print(f"{colors.bright_cyan}Profit Level: {profitLevel}{colors.ENDC}")
  print(f"{colors.bright_magenta}Multiplier: {multiplierLevel}{colors.ENDC}\n")
  print("Enter The Number To Do The Following: ")
  print(f"1 : UPGRADE FACTORY : ${round(500 * factoryCostInc)}")
  print(f"2 : UPGRADE MACHINERY : ${round(500 * machineCostInc)}")
  print("3 : UPGRADE SALARY CAP : 10 Salary Credits")
  print(f"4 : UPGRADE PROFIT : ${round(500 * profitCostInc)}")
  print(f"5 : UPGRADE MULTIPLIERS : ${round(500 * multiplierCostInc)}")
  print("6 : BUY SALARY CREDITS : $500")
  print("7 : HELP")
  print("8 : HOME SCREEN")
  upgradeChoice = input("")
  if upgradeChoice == "1":
    if money >= (500 * factoryCostInc):
      factoryLevel += 1
      money -= (500 * factoryCostInc)
      factoryCostInc = factoryCostInc + 0.5
    else:
      typing(f"{colors.red}You Do Not Have Enough Money To Upgrade Factory To Level {factoryLevel}!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Money!{colors.ENDC}\n")
      wait()
      start()
  elif upgradeChoice == "2":
    if money >= (500 * machineCostInc):
      machineryLevel += 1
      money -= (500 * machineCostInc)
      machineCostInc = machineCostInc + 0.5
    else:
      typing(f"{colors.red}You Do Not Have Enough Money To Upgrade Machinery To Level {machineryLevel}!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Money!{colors.ENDC}\n")
      wait()
      start()
  elif upgradeChoice == "3":
    if salaryCredits >= 10:
      salarycap += 500
      salaryCredits -= 10
    else:
      typing(f"{colors.red}You Do Not Have Enough Salary Credits To Upgrade Salary Cap (Max)!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Salary Credits!{colors.ENDC}\n")
      wait()
      start()
  elif upgradeChoice == "4":
    if money >= (500 * profitCostInc):
      profitLevel += 1
      money -= (500 * profitCostInc)
      profitCostInc = profitCostInc + 0.5
    else:
      typing(f"{colors.red}You Do Not Have Enough Money To Upgrade Profit To Level {profitLevel}!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Money!{colors.ENDC}\n")
      wait()
      start()
  elif upgradeChoice == "5":
    if money >= (500 * multiplierCostInc):
      multiplierLevel += 1
      money -= (500 * multiplierCostInc)
      multiplierCostInc = multiplierCostInc + 0.5
    else:
      typing(f"{colors.red}You Do Not Have Enough Money To Upgrade Multiplier To Level {multiplierLevel}!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Money!{colors.ENDC}\n")
      wait()
      start()
  elif upgradeChoice == "6":
    if money >= 500:
      salaryCredits += 5
      money -= 500
    else:
      typing(f"{colors.red}You Do Not Have Enough Money To Buy Salary Credits!{colors.ENDC}\n")
      typing(f"{colors.red}Try Again When You Have More Money!{colors.ENDC}\n")
      wait()
      start() 
  elif upgradeChoice == "7":
    clear()
    typing(f"{colors.bright_yellow}Welcome To Help Center For Upgrades!{colors.ENDC}\n\n")
    print(f"What Does {colors.bright_magenta}Option 1{colors.ENDC} Do On Upgrades Page?")
    print("Option 1 Upgrades Factory. This Increases Profit Which Can Be Really Useful!\n")
    print(f"What Does {colors.bright_magenta}Option 2{colors.ENDC} Do On Upgrades Page?")
    print("Option 2 Upgrades Machinery. This Also Increases Profit!\n")
    print(f"What Does {colors.bright_magenta}Option 3{colors.ENDC} Do On Upgrades Page?")
    print("Option 3 Upgrades Salary Cap! This Allows You To Hire More Workers And Make More Money!! Salary Cap Transactions Only Accept Salary Credits!\n")
    print(f"What Does {colors.bright_magenta}Option 4{colors.ENDC} Do On The Upgrades Page?")
    print("Option 4 Multiplies The Amount Of Profit You Make! AMAZING!!\n")
    print(f"What Does {colors.bright_magenta}Option 5{colors.ENDC} Do On The Upgrades Screen?")
    print("Option 5 Multiplies EVERYTHING To REALLY Increase Profit!! *totally not busted*\n")
    print(f"What Does {colors.bright_magenta}Option 6{colors.ENDC} Do On The Upgrades Screen?")
    print("Option 6 Allows You To Buy Salary Credits, Which Can Be Used TO Purchases A Higher Salary Cap, Which Allows You To Hire More Workers!!\n")
    input("Press Enter To Return To Factory Upgrade Screen")
    clear()
    upgrade()
  elif upgradeChoice == "8":
    clear()
    start()
  else:
    typing(f"{colors.red}Invalid Response{colors.ENDC}\n")
    typing(f"{colors.red}Please Try Again{colors.ENDC}\n")
    time.sleep(1)
    clear()
    upgrade()
    



def staff():
  global salarypaid
  print(f"{colors.bright_green}Money: ${round(money)}{colors.ENDC}")
  if (salarypaid < salarycap/2):
    print(f"Salary: {colors.bright_green}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  elif (salarycap/2 <= salarypaid <= salarycap*(3/4)):
    print(f"Salary: {colors.bright_yellow}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  elif (salarypaid > salarycap*(3/4)):
    print(f"Salary: {colors.red}${salarypaid}{colors.ENDC} Out Of ${salarycap}\n")
  typing(f"{colors.bright_magenta}Searching For Free Agents ...{colors.ENDC}\n\n")
  time.sleep(2.75)
  probfreeagents = random.choice(prob_free_agents_workers)
  if probfreeagents == 0:
    typing(f"{colors.bright_magenta}No Free Agent Found{colors.ENDC}\n")
    wait()
    start()
  else:
    worker_name = random.choice(free_agents_first_name_workers) + " " + random.choice(free_agents_last_name_workers)
    free_agent_worker_salary = random.randint((salarycap/4), salarycap)
    free_agent_worker_condition = random.choice(worker_condition)
    typing(f"{colors.bright_magenta}Free Agent Found: {colors.ENDC}")
    print(worker_name)
    typing(f"\n{colors.bright_magenta}Free Agent Salary: ${free_agent_worker_salary}{colors.ENDC}\n")
    typing(f"\n{colors.bright_magenta}Free Agent Condition: {free_agent_worker_condition}{colors.ENDC}\n")
    typing(f"\n{colors.bright_magenta}Would You Like To Hire {worker_name}? {colors.ENDC}\n")
    hire = input("Yes/No? (y/n) ")
    if hire.upper() == "YES" or hire.upper() == "Y":
      salarypaid = salarypaid + free_agent_worker_salary
      if salarypaid > salarycap:
        typing(f"{colors.red}You Do Not Have Enough Salary To Pay {worker_name}!{colors.ENDC}\n")
        typing(f"{colors.red}To Upgrade Your Salary, Purchase Salary Credits!{colors.ENDC}\n")
        typing(f"{colors.red}Salary Credits Can Be Found In Upgrade Factory!{colors.ENDC}\n")
        salarypaid = salarypaid - free_agent_worker_salary
        wait()
        start()
      else:
        typing(f"{colors.bright_magenta}You Have Hired {worker_name}!{colors.ENDC}\n\n")
        free_agents_hired.append(worker_name)
        free_agents_hired_salary.append(free_agent_worker_salary)
        free_agents_hired_condition.append(free_agent_worker_condition)
        wait()
        start()
    elif hire.upper() == "NO" or hire.upper() == "N":
      wait()
      start()
    else:
      salarypaid += 0
      typing(f"{colors.red}Invalid Answer{colors.ENDC}")
      typing(f"{colors.red}You Will Not Be Able To Hire {worker_name}!{colors.ENDC}")
      wait()
      start()

def stats():
  print(f"{colors.underline}STATS ABOUT FACTORY{colors.ENDC}\n")
  print(f"Number Of Days: {days}")
  print(f"Money: ${round(money)}")
  print(f"Number Of Employees: {len(free_agents_hired)}")
  print(f"Salary Paid To Workers: {salarypaid}")
  print(f"Salary Cap (Max): ${salarycap}\n")
  print(f"{colors.underline}FACTORY EMPLOYEES{colors.ENDC}\n")
  print(f"{colors.italic}Format - Employee Name : Employee Salary : Employee Condition{colors.ENDC}\n")
  for i in range(len(free_agents_hired)):
    print(f"{free_agents_hired[i]} : ${free_agents_hired_salary[i]} : {free_agents_hired_condition[i]}")
  print("\n")
  wait()
  start()

def quote():
  quote = random.choice(randomquote)

  typing(f"{colors.bright_cyan}{quote}{colors.ENDC}\n\n")

  wait()
  start()

def helpme():
  typing(f"{colors.bright_yellow}Welcome To Help Center!{colors.ENDC}\n\n")
  print(f"What Does {colors.bright_magenta}Option 1{colors.ENDC} Do On Main Page?")
  print("Option 1 Basically Adds An Extra Day, Like If You Were To Come Back The Next Day In A Game! If A Month (30 Days) Passes, The Amount Of Salary Paid To Your Employees Is Deducted From The Amount Of Money You Have!!\n")
  print(f"What Does {colors.bright_magenta}Option 2{colors.ENDC} Do On Main Page?")
  print("Option 2 Opens The Shop, I Explain Shop More In Detail In Shop Help Center (Press 2 [enter], 7 [enter])\n")
  print(f"What Does {colors.bright_magenta}Option 3{colors.ENDC} Do On Main Page?")
  print("Option 3 Finds New Workers For Your Business! Without Workers You Can't Do Anything!! Make Sure To BUY WORKERS Immediatly Or You Will Become Bankrupt!\n")
  print(f"What Does {colors.bright_magenta}Option 4{colors.ENDC} Do On The Main Page?")
  print("Option 4 Allows You To See All Of Your Businesses' Information! Pretty Useful When You Get A TON Of Workers!\n")
  print(f"What Does {colors.bright_magenta}Option 5{colors.ENDC} Do On The Main Screen?")
  print("Option 5 Provides Moral Boosting (And Very Intelligent) Quotes!\n")

  wait()
  start()
  



if skip.upper() == "I":
  clear()
  intro()

time.sleep(0.75)

clear()
start()

while True:
  while startChoice == "1":
    clear()
    days += 1
    money += (multiplierLevel + profitLevel)*(random.randint(10, 25)*(len(free_agents_hired)))
    if len(free_agents_hired) > 0:
      money += multiplierLevel*(factoryLevel + machineryLevel)
    if days % 30 == 0:
      money -= int(salarypaid)
    start()

  while startChoice == "2":
    clear()
    upgrade()

  while startChoice == "3":
    clear()
    staff()

  while startChoice == "4":
    clear()
    stats()
  
  while startChoice == "5":
    clear()
    quote()
  
  while startChoice == "6":
    clear()
    helpme()

  while startChoice != "1" and startChoice != "2" and startChoice != "3" and startChoice != "4" and startChoice != "5" and startChoice != "6":
    typing(f"{colors.red}Invalid Response{colors.ENDC}\n")
    typing(f"{colors.red}Please Try Again{colors.ENDC}\n")
    time.sleep(1)
    clear()
    start()



