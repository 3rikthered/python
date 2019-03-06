from random import randint

def probability(people, simulations):
  sharedBirthdaysExist = 0
  
  for i in range(simulations):
    birthdays = [randint(0, 365) for i in range(people)]
    sharedBirthdays = set(date for date in birthdays if birthdays.count(date) > 1)
    if len(sharedBirthdays) >= 1:
      sharedBirthdaysExist += 1

  return sharedBirthdaysExist / simulations * 100

print(probability(22,10000))
