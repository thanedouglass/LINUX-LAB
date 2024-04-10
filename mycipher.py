import sys
def caesar_cipher(message, shift):
  encoded_message = ""
  for char in message:
    # Check if the character is an uppercase letter
    if char.isalpha() and char.isupper():
      # Shift the character by the specified amount
      new_ord = ord(char) + shift
      # Handle wrapping around the alphabet
      new_ord = new_ord % 26 + ord('A')
      encoded_message += chr(new_ord)
  return encoded_message

def main():
    # Check if the correct number of command line arguments are provided
  if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift_amount>")
    sys.exit(1)
    
  # Get the shift amount from command line arguments
  shift = int(sys.argv[1])

  # Read the message from the keyboard (stdin)
  message = input("Enter the message: ")
    
  # Convert the message to all uppercase
  message = message.upper()
    
  # Encode the message using Caesar Cipher
  encoded_message = caesar_cipher(message, shift)

    # Print the final encoded message in blocks of five letters
  block_size = 5
  for i in range(0, len(encoded_message), block_size):
    print(encoded_message[i:i+block_size], end=" ")
    # Print newline after every five blocks
    if (i+1) % (block_size * 10) == 0:
      print()

if __name__ == "__main__":
    main()
