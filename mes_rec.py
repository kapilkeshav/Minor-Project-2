import cipher
import WhsiperF
import client
def mes_rec():
    dec = WhsiperF.decode()
    dec_fin = cipher.decrypt(dec)
    return dec_fin
    
