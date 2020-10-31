import sqlite3, colorama, os, random, datetime
from shutil import rmtree as rm

colorama.init()

class auth(object):

    def __init__(self):
        self.username, self.password = "", ""
        self.loggedIn = False

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        # CHECK USERNAME IN DATABASE
        # USE DATABASE THTA HIDES USER DATA
        #FOR TESTING PURPOSES ONLY!!!
        if username == "Dextron" and password == "Hashcoder":
            self.loggedIn = True
            self.username, self.password = username, password
        
    def createUser(self):
        print("This function is currently not available")

    def logout(self):
        self.username, self.password = "", ""
        self.loggedIn = False
        self.login()

class Vault(object):

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        self.keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '[', '{', ']', '}', '?', '<', '>', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    def generateKeys(self, genNumber, keyNumber, keyChar=1, notChar=False):
        # GEN NUMBE RIS THE NUMBER OF KEY LISTS TO BE GENERATED 
        # KEY NUMBER IS HOW MANY KEYS SHOULD BE INCLUDED IN EACH KEY LIST
        # KEY CHAR IS HOW MANY CHARS ARE USED FOR ONE KEY
        # NOT CHAR IS WHERE A CHAR AHS A CHANCE IN REMAINING THE SAME
        genKey = {}
        for key in range(keyNumber):
            currentKey = []
            if str(key) not in genKey:
                for letter in self.keys:
                    # GET RANDOM KEY FOR THE SLECTED KEY | h = *?
                    if keyChar != 1:
                        for i in range(keyChar):
                            randomChar = random.choice(self.keys)
                            if notChar == True:
                                while randomChar == letter:
                                    randomChar = random.choice(self.keys)
                            genKey[randomChar] = letter # RANDOM ENCRYPTION = ACTUAL DECRYPT LETTER
                    else:
                        randomChar = random.choice(self.keys)
                        if notChar == True:
                            while randomChar == letter:
                                randomChar = random.choice(self.keys)
                        genKey[randomChar] = letter
        return genKey
        # USE THIS TO DECRYPT 
        # list(dict.keys())[list(d.values()).index("Actual Letter")]
                            

                        #for how ever many chars for one key generate it

    def decrypt(self, code, encryptionKeys, keySize=1):
        decryptCode = []
        if keySize == 1:
            for char in code:
                decryptCode.append(encryptionKeys[char])
                # DECIPHERS EACH CHAR BY CCHAR AND APPENDS TO decryptCode LIST
        else:
            # YAY THE FUN PART!!
            # IF CODE IS USING MULTIPLE CHARS FOR SINGLE LETTER DECRYPT!!
            # DECRYPT BY USING THE CHARSIZE TO CHECK IF IT IS DEVISIBLE BY THE CODE CHAR SIZE
            # IF SO THEN WE USE THE SELECTED SIZE OF CODE AND CHECK IN OUR ENCRIPTION KEYS
            # IF IT IS FOUND IN ENCRYPTION KEYS THEN APPEND TO decryptCode LIST
            # IF NOT ASSUME THE CODE IS BROKEN OR TAMPERED WITH 
            # ALERT USER READING IT AND DUMP AND DEADLOCK VAULT
            for char in range(len(code)):
                if char % keySize == 0:
                    # get prev chaars using the theritical known amount of char length
                else:
                    # THOIS WILL HAPPEN IN GENERAL FOR THE LARGE CHAR STRINGS
                    pass

    def encrypt(self, text, encryptionKeys, keySize=1):
        encryptedCode = []
        if keySize == 1:
            # THE EASY PART
            # SEARCH FOR THE LETTER IN THE DICT THEN GRAP THE ENCRYPTOR
            # BREAK THE TETX INTO CHARS FOR EASY ENCRYPT
            for char in text:
                encryptedCode.append(list(encryptionKeys.keys())[list(encryptionKeys.values()).index(char)])
        else:
            # DO ENCRYPTION FOR MULTICHAR CHARACTERS
            pass
        return encryptedCode
                



            


    def new_vault(self):
        while True:
            print(colorama.ansi.clear_screen())
            vaultName = input("Enter Vault Name: ")
            os.mkdir(self.BASE_DIR + '//Vaults//%s' % (vaultName))
            genEncrypt = input("Create Random Encryption Set (Y|N): ")
            if genEncrypt == 'Y' or 'y' or 'yes' or 'YES':
                with open(self.BASE_DIR + '//Vaults//%s//keys.vault' % (vaultName), 'w') as f:
                    encryptionKey = self.generateKeys(1, 26)
                    f.write(encryptionKey + "{~}" + str(datetime.now()))
                break
            else:
                # USER DOESNT WANT VUALT ENTRIES ENCRYPTED
                with open(self.BASE_DIR + "//Vaults//%s//keys.vault" % (vaultName), 'w') as f:
                    f.write("No_Encrypt")
                break
        return vaultName

    def load_vault(self, vaultName):
        with open(self.BASE_DIR + '//Vaults//%s//keys.vault' % (vaultName), 'r') as f:
            data = f.read()
        if data != "No_Encrypt":
            time = data.split("{~}")[1]
            encryptionKey = data.split("{~}")[0]
        else:
            encryptionKey = {}
            for char in vault.keys:
                encryptionKey[char] = char
                time = datetime.now()
        return encryptionKey, time

    def delete_vault(self, vaultName):
        if self.BASE_DIR + "//Vaults" in vaultName:
            while True:
                sure = input("Delete %s Vault (Y|N): " % (vaultName))
                if sure == "Y" or "y" or "yes" or "YES":
                    rm(vaultName)
                elif sure == "N" or "n" or "no" or "NO":
                    break 

    def new_msg(self, vaultName, encryptionKey, msgFile=None):
        if msgFile == None:
            while True:
                msgName = input("Vault Entry Name: ")
                msg = input("Entry: ")
                if os.path.isdir(self.BASE_DIR + "//Vaults//%s//" % (vaultName)):
                    if list(encryptionKey.keys()) != list(encryptionKey.value()):
                        msg = self.encrypt(msg, encryptionKey)
                        with open(self.BASE_DIR + "//Vaults//%s//%s.msg" % (vaultName, str(datetime.now())), 'w') as f:
                            f.write(msg)
                    else:
                        # MSG DOES NOT REQUIRE ANY ENCRYPTION | JUST DUMP IN PLAIN TEXT
                        with open(self.BASE_DIR + "//Vaults//%s//%s" % (vaultName, datetime.now(), 'w') as f:
                            f.write(msg)

    def read_msg(self, vaultName, fileName)
                    

                    



                




class Loader(object):

    def menu(self):
        vaultName = None
        while True:
            print(colorama.ansi.clear_screen())
            print("Hashcoder V0.1 Beta")
            print("")
            print("1. New Vault\n")
            print("2. Load Vault\n")
            print("3. Save Vault\n")
            print("4. Delete Vault\n")
            print("5. Encrypt Message to Vault\n")
            print("6. Decrypt Message from Vault\n")
            controller = input("Select An Option: ")
            if controller == 1:
                vaultName = vault.new_vault() 
                encryptionKey, time = vault.load_vault()
            elif controller == 2:
                encryptionKey, time = vault.load_vault()
            elif controller == 3:
                pass # DO SAVE VAULT FUNCTION
            elif controller == 4:
                vault.delete_vault()
            elif controller == 5:
                if vaultName != None and encryptionKey != None:
                    while True:
                        fileControl = input("Load Message from file (Y|N): ")
                        if fileControl == "y" or "yes" or "YES" or "Y":
                            fileHeader = input("File Name: ")
                            with open(fileHeader, 'r') as f:
                                fileHeader = f.read()
                            vault.new_msg(vaultName, encryptionKey, fileHeader)
                        else:
                            vault.new_msg(vaultName, {})

            elif controller == 6:

loader = Loader()
vault = Vault()

loader.menu()



