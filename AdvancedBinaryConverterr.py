import time as t 
binary_negative = False
binary_twos_complement = False
negative = False
twos_complement = False

def binary_to_decimal():
  global binary_negative
  global binary_twos_complement

  binary_input = input("Enter a Binary Number: ")
  if '.' in binary_input:
    print("Invalid Input - Decimal Point Detected\n")
    menu()
    return

  binary = list(map(int, binary_input))

  if binary[0] == 1:
    conversion_type = int(input("What Type of Conversion Do You Want to Use?\n1) Standard - Non-Negative Number\n2) Sign and Magnitude\n3) Two's Complement\n"))

    if conversion_type == 1:
      binary_negative = False
      decimal_number = binary_conversion(binary)
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)}\n")

    elif conversion_type == 2:
      binary_negative = True
      decimal_number = binary_conversion(binary)
      decimal_number *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)} When Converted Using Sign and Magnitude\n")

    elif conversion_type == 3:
      binary_twos_complement = True
      decimal_number = binary_conversion(binary)
      decimal_number *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)} When Converted Using Two's Complement\n")

def binary_conversion(binary):
  if binary_negative and binary[0] == 1:
    binary.pop(0)  # Remove sign bit for sign and magnitude
  if binary_twos_complement:
    for i in range(len(binary)):
      binary[i] = 1 - binary[i]  # Invert bits for two's complement
    carry = 1
    for i in range(len(binary)):
      binary[i] += carry
      if binary[i] > 1:
        binary[i] = 0
        carry = 1
      else:
        carry = 0

  decimal = 0
  bitlength = 2 ** (len(binary) - 1)

  for bit in binary:
    if bit == 1:
      decimal += bitlength
    bitlength /= 2

  return decimal

def decimal_to_binary():
  global negative
  global twos_complement

  decimal = int(input("Enter a Decimal Number: "))

  if decimal < 0:
    conversion_type = int(input("Would You Like to Convert This Number Using:\n1) Sign and Magnitude\n2) Two's Complement\n"))

    if conversion_type > 2 or conversion_type < 1:
      print("Invalid Choice - 1 for Sign and Magnitude and 2 for Two's Complement\n")
      decimal_to_binary()

    elif conversion_type == 1:
      negative = True
      twos_complement = False
      decimal = -decimal
      binary_number = decimal_conversion(decimal)
      print(f"\n{decimal} Converted Using Sign and Magnitude to a Binary Number is {binary_number}\n")

    elif conversion_type == 2:
      twos_complement = True
      negative = False
      decimal = -decimal
      binary_number = decimal_conversion(decimal)
      decimal = -decimal
      print(f"\n{decimal} Converted Using Two's Complement to a Binary Number is {binary_number}\n")

  else:
    binary_number = decimal_conversion(decimal)
    print(f"\n{decimal} Converted Using Standard Binary Conversion is {binary_number}\n")

def decimal_conversion(decimal):
  binary = []

  while decimal > 0:
    remainder = decimal % 2
    binary.append(remainder)
    decimal = decimal // 2

  if negative:
    binary.append(1)  # Add sign bit for sign and magnitude

  if twos_complement:
    while len(binary) % 2 != 0:
      binary.append(0)  # Pad to even length for two's complement

    for i in range(len(binary)):
      binary[i] = 1 - binary[i]  # Invert bits for two's complement

    carry = 1
    for i in range(len(binary)):
      binary[i] += carry
      if binary[i] > 1:
        binary[i] = 0
        carry = 1
      else:
        carry = 0

  binary_number = "".join(map(str, binary[::-1]))
  return binary_number

def fractional_binary_to_decimal():
  global binary_negative
  global binary_twos_complement
  binary_input = input("Enter a Binary Number: ")
  binary = list(map(str, binary_input))
  for i in range(len(binary)):
    if binary[i] != '.':
      binary[i] = int(binary[i])
  print("working")
  if binary[0] == 1:
    conversion_type = int(input("What Type of Conversion Do You Want to Use?\n1) Standard - Non-Negative Number\n2) Sign and Magnitude\n3) Two's Complement\n"))
    if conversion_type == 1:
      binary_negative = False
      decimal = fractional_binary_conversion(binary)
      return decimal
    elif conversion_type == 2:
      binary_negative = True
      decimal = fractional_binary_conversion(binary)
      decimal *= -1
      binary.insert(0, 1)
      binary = "".join(map(str, binary))

      print(f"\n{binary} is Equal to {decimal} When Converted Using Sign and Magnitude\n")
    elif conversion_type == 3:
      binary_twos_complement = True
      decimal = fractional_binary_conversion(binary)
      decimal *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {decimal} When Converted Using Two's Complement\n")
    else:
      print("Invalid Choice\n")
      t.sleep(1)
      fractional_binary_to_decimal()
  else:
    decimal = fractional_binary_conversion()
    decimal = fractional_binary_conversion(binary)
    print(f"\n{binary} is Equal to {decimal}\n")
def fractional_binary_conversion(binary):
  if binary_negative:
    binary.pop(0)
  if '.' in binary:
    decimal_point = binary.index('.')
    decimal = 0
    integers = list(map(int, binary[:decimal_point]))
    fractions = list(map(int , binary[decimal_point + 1:]))
    bitlength = 2 ** (len(integers) - 1)
    print(bitlength)
    print(integers)
    if binary_twos_complement:
      while len(integers) % 4 != 0:
        integers.append(0)
      for i in range(len(integers)):
        if integers[i] == 1:
          integers[i] = 0
        else:
          integers[i] = 1
      carry = 1
      integers = integers[::-1]
      for i in range(len(integers)):
        integers[i] += carry
        if integers[i] > 1:
          integers[i] = 0
          carry = 1
        else:
          carry = 0
      integers = integers[::-1]
      print(integers)
    for bit in integers:
      if bit == 1:
        decimal += bitlength
      bitlength /= 2
    print(decimal)
    fractional_bit_length = 0.5
    for bit in fractions:
      if bit == 1:
        decimal += fractional_bit_length
      fractional_bit_length /= 2
    binary = "".join(map(str, binary))
    return decimal

  else:
    print("Invalid Input - No Decimal Point\n")
    t.sleep(1)
    fractional_binary_to_decimal()

def fractional_decimal_to_binary():
  global negative
  global twos_complement
  decimal = float(input("Enter a Decimal Number: "))
  if decimal < 0:
    conversion_type = int(input("Would You Like to Convert This Number Using:\n1) Sign and Magnitude\n2) Two's Complement\n")) 
    if conversion_type > 2 or conversion_type < 1:
      print("Invalid Choice - 1 for Sign and Magnitude and 2 for Two's Complement\n")
      fractional_decimal_to_binary()
    elif conversion_type == 1:
      negative = True
      twos_complement = False
      decimal = -decimal
      binary_number = fractional_decimal_conversion(decimal)
      decimal = -decimal
      print(f"\n{decimal} Converted Using Sign and Magnitude to a Binary Number is {binary_number}\n")
    elif conversion_type == 2:
      twos_complement = True
      negative = False
      decimal = -decimal
      binary_number = fractional_decimal_conversion(decimal)
      decimal = -decimal
      print(f"\n{decimal} Converted Using Two's Complement to a Binary Number is {binary_number}\n")
  fractional_decimal_conversion(decimal)

def fractional_decimal_conversion(decimal):
  print("Fractional Decimal to Binary Conversion\n")
  binary = []
  integer = int(decimal)
  fraction = decimal - integer
  # print(decimal)
  # print(binary)
  # print(integer)
  while integer > 0:
    remainder = integer % 2
    binary.append(remainder)
    integer = integer // 2
  print(binary)
  if twos_complement:
    while len(binary) % 4 != 0:
      binary.append(0)  # Pad to even length for two's complement

    for i in range(len(binary)):
      binary[i] = 1 - binary[i]  # Invert bits for two's complement

    carry = 1
    for i in range(len(binary)):
      binary[i] += carry
      if binary[i] > 1:
        binary[i] = 0
        carry = 1
      else:
        carry = 0

  binary = binary[::-1]
  binary.append('.')
  fraction_start = 0.5
  while fraction > 0:
    if fraction - fraction_start >= 0:
      binary.append(1)
      fraction -= fraction_start
      fraction_start /= 2
  if negative:
    binary.insert(0, 1)
  binary = "".join(map(str, binary))
  return binary


def menu():
  conversion_type = input("Enter 1 to Convert Binary to Decimal or 2 to Convert Decimal to Binary or 3 to Convert Fractional Binary to Decimal or 4 to Convert Fractional Decimal to Binary: ")

  if conversion_type == '1':
    binary_to_decimal()
  elif conversion_type == '2':
    decimal_to_binary()
  elif conversion_type == '3':
    fractional_binary_to_decimal()
  elif conversion_type == '4':
    fractional_decimal_to_binary()
  else:
    print("Invalid Choice\n")
    menu()
menu()