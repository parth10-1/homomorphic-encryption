import random

class Encryption:
    def __init__(self, public_key_prime, public_key_alpha, public_key_beta, input_plain_text):
        #Initializing ENcryption
        self.public_key_prime = public_key_prime #int(input(f"Enter public key prime: "))
        self.public_key_alpha = public_key_alpha #int(input(f"Enter public key alpha: "))
        self.public_key_beta  = public_key_beta  #int(input(f"Enter public key beta: "))
        self.input_plain_text = input_plain_text #int(input(f"Enter plain text to encrypt: "))
        self.cipher_text_x = 0
        self.cipher_text_y = 0

    def encrypt_plaintext(self):

        encry_int = self._generate_random_int()

        self.cipher_text_x = (pow(self.public_key_alpha, encry_int, self.public_key_prime))
        self.cipher_text_y = (pow(self.public_key_alpha, self.input_plain_text, self.public_key_prime) * pow(self.public_key_beta, encry_int, self.public_key_prime)) % self.public_key_prime

        return (self.cipher_text_x, self.cipher_text_y)

    def _generate_random_int(self):
        return random.randint(2, self.public_key_prime - 2)