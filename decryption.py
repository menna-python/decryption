import string
user_message=input("Please enter your message\n")
user_shift=int(input("Please enter shifting number\n"))
def decrypt(message,shift):
  decrypted_message=""
  for letter in message:
    alphabet=string.ascii_lowercase
    if letter.lower() not in alphabet:
      decrypted_message+=letter
      continue
    else:
      original_position=alphabet.index(letter.lower())
      new_position=(original_position-shift)%26
      decrypted_letter=alphabet[new_position]
    if letter.isupper():
      decrypted_letter=decrypted_letter.upper()
      decrypted_message+=decrypted_letter
    else:
      decrypted_message+=decrypted_letter
  print(f"Decrypted message is {decrypted_message}")
decrypt(message=user_message,shift=user_shift)
      