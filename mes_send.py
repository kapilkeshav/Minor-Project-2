import cipher
import WhsiperF
import client
def mes_send(message):
    enc = cipher.encrypt(message)
    fin_enc = WhsiperF.encode(enc)
    client.s_msg()

