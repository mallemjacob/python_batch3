# parameter weekday is True if it is a weekday
# parameter vacation is True if we are on vacation
# not weekday or vacation
# return True if we sleep in.   

# not a weekday or we're on vacation --> sleep in --> return True


def sleep_in(weekday, vacation):
  if weekday != "True" or vacation == "True":
    print("True")
  else:
    print("False")

n1 = input('weekday: ')
n2 = input('vacation: ')
sleep_in(n1,n2)