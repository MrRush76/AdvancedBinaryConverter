
import time as t 
binary_negative = False
binary_twos_complement = False
negative = False
twos_complement = False

def binary_to_decimal():
  """
  Converts a binary number to its decimal equivalent.
  This function prompts the user to input a binary number and converts it to a decimal number.
  It handles three types of conversions:
  1. Standard - Non-Negative Number
  2. Sign and Magnitude
  3. Two's Complement
  The function performs the following steps:
  1. Takes binary input from the user.
  2. Validates the input to ensure it is a binary number.
  3. If the binary number is negative (starts with 1), prompts the user to choose a conversion type.
  4. Converts the binary number to its decimal equivalent based on the chosen conversion type.
  5. Prints the decimal equivalent of the binary number.
  6. Calls the menu function to display the menu options again.
  Global Variables:
  - binary_negative: A flag indicating if the binary number is negative.
  - binary_twos_complement: A flag indicating if the conversion type is Two's Complement.
  Raises:
  - ValueError: If the input contains non-binary digits or a decimal point.
  Note:
  - The function assumes the existence of the `binary_conversion` and `menu` functions.
  """
  global binary_negative
  global binary_twos_complement

  binary_input = input("Enter a Binary Number: ")
  if '.' in binary_input:
    print("Invalid Input - Decimal Point Detected\n")
    menu()
    return
  try:
    binary = list(map(int, binary_input))
  except ValueError:
    print("Invalid Input - Binary Numbers Only\n")
    menu()
    return
  for i in range(len(binary)):
    if binary[i] != 0 and binary[i] != 1:
      print("Invalid Input - Binary Numbers Only\n")
      menu()
      return
  if binary[0] == 1:
    conversion_type = int(input("What Type of Conversion Do You Want to Use?\n1) Standard - Non-Negative Number\n2) Sign and Magnitude\n3) Two's Complement\n"))

    if conversion_type == 1:
      binary_negative = False
      decimal_number = binary_conversion(binary)
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)}\n")
      menu()

    elif conversion_type == 2:
      binary_negative = True
      decimal_number = binary_conversion(binary)
      decimal_number *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)} When Converted Using Sign and Magnitude\n")
      menu()

    elif conversion_type == 3:
      binary_twos_complement = True
      decimal_number = binary_conversion(binary)
      decimal_number *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {int(decimal_number)} When Converted Using Two's Complement\n")
      menu()
  else:
    decimal_number = binary_conversion(binary)
    binary = "".join(map(str, binary))
    print(f"\n{binary} is Equal to {int(decimal_number)}\n")
    menu()
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
  try:
    decimal = int(input("Enter a Decimal Number: "))
  except ValueError:
    print("Invalid Input - Integers Only\n")
    menu()
    return

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
      decimal = -decimal
      print(f"\n{decimal} Converted Using Sign and Magnitude to a Binary Number is {binary_number}\n")
      menu()
    elif conversion_type == 2:
      twos_complement = True
      negative = False
      decimal = -decimal
      binary_number = decimal_conversion(decimal)
      decimal = -decimal
      print(f"\n{decimal} Converted Using Two's Complement to a Binary Number is {binary_number}\n")
      menu()

  else:
    binary_number = decimal_conversion(decimal)
    print(f"\n{decimal} Converted Using Standard Binary Conversion is {binary_number}\n")
    menu()
def decimal_conversion(decimal):
  binary = []

  while decimal > 0:
    remainder = decimal % 2
    binary.append(remainder)
    decimal = decimal // 2

  if negative:
    binary.append(1)  # Add sign bit for sign and magnitude

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

  binary_number = "".join(map(str, binary[::-1]))
  return binary_number

def fractional_binary_to_decimal():
  global binary_negative
  global binary_twos_complement
  binary_input = input("Enter a Binary Number: ")
  binary = list(map(str, binary_input))
  for i in range(len(binary)):
    if binary[i] != '.':
      try:
        binary[i] = int(binary[i])
      except ValueError:
        print("Invalid Input - Binary Numbers Only\n")
        menu()
        return
  if binary[0] == 1:
    conversion_type = int(input("What Type of Conversion Do You Want to Use?\n1) Standard - Non-Negative Number\n2) Sign and Magnitude\n3) Two's Complement\n"))
    if conversion_type == 1:
      binary_negative = False
      decimal = fractional_binary_conversion(binary)
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {decimal}\n")
    elif conversion_type == 2:
      binary_negative = True
      decimal = fractional_binary_conversion(binary)
      decimal *= -1
      binary.insert(0, 1)
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {decimal} When Converted Using Sign and Magnitude\n")
      menu()
    elif conversion_type == 3:
      binary_twos_complement = True
      decimal = fractional_binary_conversion(binary)
      decimal *= -1
      binary = "".join(map(str, binary))
      print(f"\n{binary} is Equal to {decimal} When Converted Using Two's Complement\n")
      menu()
    else:
      print("Invalid Choice\n")
      t.sleep(1)
      fractional_binary_to_decimal()
  else:
    try:
      decimal = fractional_binary_conversion(binary)
    except ValueError:
      print("Invalid Input - No Decimal Point\n")
      menu()
    print(f"\n{binary} is Equal to {decimal}\n")
    menu()
def fractional_binary_conversion(binary):
  if binary_negative:
    binary.pop(0)
  if '.' in binary:
    decimal_point = binary.index('.')
    decimal = 0
    integers = list(map(int, binary[:decimal_point]))
    fractions = list(map(int , binary[decimal_point + 1:]))
    bitlength = 2 ** (len(integers) - 1)
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
    for bit in integers:
      if bit == 1:
        decimal += bitlength
      bitlength /= 2
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
  try:
    decimal = float(input("Enter a Decimal Number: "))
  except ValueError:
    print("Invalid Input - Integers Only\n")
    menu()
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
      menu()
    elif conversion_type == 2:
      twos_complement = True
      negative = False
      decimal = -decimal
      binary_number = fractional_decimal_conversion(decimal)
      decimal = -decimal
      print(f"\n{decimal} Converted Using Two's Complement to a Binary Number is {binary_number}\n")
      menu()
  num1 = fractional_decimal_conversion(decimal)
  print(f"\n{decimal} Converted to a Binary Number is {num1}\n")
  menu()

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
  conversion_type = input(
    "Enter the conversion type:\n"
    "1) Binary to Decimal\n"
    "2) Decimal to Binary\n"
    "3) Fractional Binary to Decimal\n"
    "4) Fractional Decimal to Binary\n"
    "Your choice: "
  )

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