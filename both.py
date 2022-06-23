# Ryan lira June 19, 2022
# veginere encryption/decryption
# this code is for anyone who finds it

edgar = ['☭','α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','π','ρ','σ','τ','υ','φ','χ','ψ','ω','0','a','“','A','\'','’','{','}',']','[','b','1','B','c','2','C','3','d','D','e','6','/','\\','5','4','E','f','F','g','7','G','h','8','9','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',' ','.',',','!','?','@','#','$','%','^','&','*','(',')','-','_','+','=',':',';','"',]

#edgar = ['0','a','“','A','\'','’','{','}',']','[','b','1','B','c','2','C','3','d','D','e','6','/','\\','5','4','E','f','F','g','7','G','h','8','9','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',' ','.',',','!','?','@','#','$','%','^','&','*','(',')','-','_','+','=',':',';','"',]
#edgar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','!','?']
print("e to encrypt.")
print("d to decrypt.")
print("any other letter to exit.")
print()
print()

x = input("encryption(e) or decryption(d): ")
while(x == 'e' or x == 'd'):
	if(x == 'e'):
		message = input("message: ")
		print()
		first = input("key: ")

###  key ################################################
		key = [None] * len(first)
		for n in range(len(first)):
			key[n] = first[n]
    
		for n in range(len(key)):
			key[n] = edgar.index(key[n])

## input #####################################################
		message_as_a_list = [None] * len(message)

		for n in range(len(message)):
			message_as_a_list[n] = edgar.index(message[n])

# encrypt message_as_a_list
		for n in range(len(message_as_a_list)):
			message_as_a_list[n] = (message_as_a_list[n] + key[n % len(key)]) % len(edgar)

#translate encrypted numbers into encrypted letters
		message_as = [None] * len(message_as_a_list)
    
		for n in range(len(message_as_a_list)):
			message_as[n] = edgar[message_as_a_list[n]]
    
		n = "".join(message_as)
		print()
		print(n)
		print()
		x = input("encryption(e) or decryption(d): ")
##############################################################
##############################################################
	if(x == 'd'):
		message = input("message: ")
		print()
		first = input("key: ")


### enter key ###############################
		key = [None] * len(first)
		for n in range(len(first)):
			key[n] = first[n]
    
		for n in range(len(key)):
			key[n] = edgar.index(key[n])

#take an encrypted string and turn into a list of numbers

		message_as_a_list = [None] * len(message)

		for n in range(len(message)):
			message_as_a_list[n] = edgar.index(message[n])

#decrypt the list of numbers
		for n in range(len(message_as_a_list)):
			message_as_a_list[n] = (message_as_a_list[n] - key[n % len(key)]) % len(edgar)

#turn the list into a string
		message_as = [None] * len(message_as_a_list)
    
		for n in range(len(message_as_a_list)):
			message_as[n] = edgar[message_as_a_list[n]]
    
		n = "".join(message_as)
		print()
		print(n)
		print()
		x = input("encryption(e) or decryption(d): ")
#nice