def alphabet_creator():
    table = {}  #{a:0,b:1}
    ctr=0
    table['a']=ctr
    for i in 'b!cd@ef#gh$ij%kl^mn&op*qr(st)uv-wx+yz=':
        ctr+=1
        table[i]=ctr
        
    return table

def output_table():                                 #Main hash table
    table = {}
    s = 'ab!cd@ef#gh$ij%kl^mn&op*qr(st)uv-wx+yz='
    for i in range(0,39):
        table[i]=s[i]
    return table

def hash_func_encr(alpha,key):
    hash_key = (alpha+key)%39
    return hash_key

def hash_func_decr(alpha,key):
    hash_key = (alpha-key)%39
    return hash_key

def encrypt(text):
    check = alphabet_creator()
    fin = output_table()
    encrypt=''
    #text = text.replace(" ","")
    for i in text:
        if i == " ":
            encrypt+=" "
        else:
            val = check[i]
            key = hash_func_encr(val,2)
            encrypt+=fin[key]
    return encrypt

def decrypt(text):
    check = alphabet_creator()
    fin = output_table()
    decrypt = ''
    #text = text.replace(" ","")
    for i in text:
        if i == " ":
            decrypt+=" "
        else:
            val = check[i]
            key = hash_func_decr(val,2)
            decrypt+=fin[key]
    return decrypt



