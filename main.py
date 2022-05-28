n = int(input("Enter  number: "))
sum = 0

for num in range(1, n + 1, 1):
  try:
    sum = sum + num
    average = sum / n
  except ValueError as e:
    print("Invlaid integer")
  print("Average of", n, "numbers is: ", average)
