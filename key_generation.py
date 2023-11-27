import random
from Crypto.Util import number

class KeyGeneration():
    def __init__(self):
        # Initializing KeyGeneration
        self.prime_num = 0
        self.number_of_coprime = 0
        self.alpha = 0
        self.prvt_key_int = 0
        self.beta = 0

    def generate_key(self):
        self.prime_num = self._prime_number_generation()
        self.number_of_coprime = self.prime_num - 1
        self.alpha = self._random_primitive_element()
        self.prvt_key_int = random.randint(1, self.prime_num - 2)
        self.beta = self._generate_beta()

        public_key = (self.prime_num, self.alpha, self.beta)
        private_key = self.prvt_key_int

        return public_key, private_key

    def _prime_number_generation(self):
        # Large prime number: 'P'
        return number.getPrime(5)

    def _random_primitive_element(self):
        # Generate and select a random primitive element
        primitive_element = []

        for i in range(3, self.prime_num, 2):
            is_primitive = True

            for k in range(1, self.number_of_coprime):
                if pow(i, k, self.prime_num) == 1:
                    is_primitive = False
                    break

            if is_primitive:
                primitive_element.append(i)

        return random.choice(primitive_element)

    def _generate_beta(self):
        # Calculate beta
        return pow(self.alpha, self.prvt_key_int, self.prime_num)
