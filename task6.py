numOfTicket = 545455 # Номер билета

print(numOfTicket)

firstSum = int(numOfTicket/100000) + int(numOfTicket/10000)%10 + int(numOfTicket/1000)%10
secondSum = int(numOfTicket/100)%10 + int(numOfTicket/10)%10 + int(numOfTicket)%10

print(firstSum)
print(secondSum)

if firstSum == secondSum :
    print(f"Билет под номером {numOfTicket} счастливый")
else :
    print(f"Билет под номером {numOfTicket} обычный")