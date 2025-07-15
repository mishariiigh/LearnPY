#  [] indexing operator

credit_number = "1234-5677-8912-2414"

#print(credit_number[0]) # print first digit
#print(credit_number[0:4]) #print from 0 to 4
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-3])#when its negative it goes from end number to begining left to right
#print(credit_number[::2])#print every second character with the string


#credit_number = credit_number[::-1] #print credit number backwards
#print(credit_number)

last_digit = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digit}")