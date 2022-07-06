class Accounts:
    def __init__(self):
        self.uuid = 0

    def fetchData(self, payload):
        # Server post UUID and get account object as jwt
        return payload

    def decryptJWT(self, jwt):
        # test and decrypt a jwt to an actual object
        return jwt

    def login(self):
        # test form entries
        # hash password
        # send hash to server
        return False

    def getCurrentAccount(self):
        jwt = self.fetchData("uuid")
        account = self.decryptJWT(jwt)
        currentAccount = account
