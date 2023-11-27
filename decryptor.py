class Decryption:
    def __init__(self, private_key, public_key_prime, public_key_alpha, ciphered_text_x, ciphered_text_y ):
      #Initializing Decryption
        self.private_key = private_key
        self.public_key_prime = public_key_prime
        self.public_key_alpha = public_key_alpha
        self.ciphered_text_x  = ciphered_text_x
        self.ciphered_text_y  = ciphered_text_y

        self.decrypted_text = 1

    def decrypt_cipher_text(self):
        m_star = self._calculate_m_star()

        current_value = self.public_key_alpha
        while current_value != m_star:
            self.decrypted_text += 1
            current_value = (current_value * self.public_key_alpha) % self.public_key_prime

        return self.decrypted_text



    def _calculate_m_star(self):
        return (pow(self.ciphered_text_x, -self.private_key, self.public_key_prime) * self.ciphered_text_y) % self.public_key_prime