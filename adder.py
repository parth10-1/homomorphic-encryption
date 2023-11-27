class Addition:
    def __init__(self, public_key_prime, cipher_x_1, cipher_y_1, cipher_x_2, cipher_y_2):
      #Initializing Addition
        self.public_key_prime = public_key_prime
        self.cipher_x_1 = cipher_x_1
        self.cipher_y_1 = cipher_y_1
        self.cipher_x_2 = cipher_x_2
        self.cipher_y_2 = cipher_y_2
        self.cipher_x_result = 0
        self.cipher_y_result = 0
        

    def add_numbers(self):
        self.cipher_x_result = (self.cipher_x_1 * self.cipher_x_2) % self.public_key_prime
        self.cipher_y_result = (self.cipher_y_1 * self.cipher_y_2) % self.public_key_prime

        return (self.cipher_x_result, self.cipher_y_result)