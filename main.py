import streamlit as st
from key_generation import KeyGeneration
from encryptor import Encryption
from decryptor import Decryption
from adder import Addition

if __name__ == '__main__':

    st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded")

    st.title("Homomorphic Encryption")

    # Sidebar
    st.sidebar.header("What's next?")


    clicked = st.sidebar.radio("Select one:", ["Key Generation", "Encryption", "Decryption", "Addition"])
    cipher_text = ()


    if clicked == "Key Generation":
        generate = st.button("Generate Key")
        if generate:
            key = KeyGeneration()
            x, y = key.generate_key()
            pub_prime, pub_alpha, pub_beta = x
            st.markdown(f'''**Public key:**  
                            [Prime number:{pub_prime}  
                             Alpha:       {pub_alpha}  
                             Beta:        {pub_beta}]  
                            Private key: {y}''')
        

    elif clicked == "Encryption":
        with st.form("Encryp"):
            st.write("Enter the following values: ")
            public_prime = int(st.number_input("Enter public key prime:  "))
            public_alpha = int(st.number_input("Enter public key alpha: "))
            public_beta = int(st.number_input("Beta"))
            plain_text = int(st.number_input("Plain text"))

            e_done = st.form_submit_button("Done!")
            if e_done:
                encry = Encryption(public_prime, public_alpha, public_beta,plain_text)
                cipher_text = encry.encrypt_plaintext()
                st.write(cipher_text)

    elif clicked == "Decryption":
        with st.form("Decryp"):
            st.write("Enter the following values: ")
            public_prime = int(st.number_input("Enter public key prime:  "))
            public_alpha = int(st.number_input("Enter public key alpha: "))
            private_key = int(st.number_input("Private key"))
            cipher_x = int(st.number_input("Encrypted value 1"))
            cipher_y = int(st.number_input("Encrypted value 2"))
            
            d_done = st.form_submit_button("Done!")
            if d_done:
                decry = Decryption(private_key, public_prime, public_alpha, cipher_x, cipher_y)
                decrypted_text = decry.decrypt_cipher_text()
                st.write(decrypted_text)

    elif clicked == "Addition":
        with st.form("Addn"):
            st.write("Enter the following values: ")
            public_prime = int(st.number_input("Enter public key prime:  "))
            cipher_x_1 = int(st.number_input("Encrypted first value 1"))
            cipher_y_1 = int(st.number_input("Encrypted first value 2"))
            cipher_x_2 = int(st.number_input("Encrypted second value 1"))
            cipher_y_2 = int(st.number_input("Encrypted second value 2"))

            a_done = st.form_submit_button("Done!")
            if a_done:
                sum = Addition(public_prime, cipher_x_1, cipher_x_2, cipher_y_2)
                result = sum.add_numbers()


