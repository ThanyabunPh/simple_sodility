from flask import Flask, request
from config import Config
from web3 import Web3

app = Flask(__name__)
app.config.from_object(Config)


class blockChain:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(Config.GANACHE_URL))
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.contract = self.web3.eth.contract(address=Config.ABI_ADDRESS, abi=Config.ABI)

    def setEmployee(self, firstName, lastName, salary):
        self.contract.functions.setEmployee(firstName, lastName, salary).transact()

    def getEmployee(self):
        return self.contract.functions.retrieveAll().call()

    def getFirstName(self):
        return self.contract.functions.retrieveFname().call()

    def getLastName(self):
        return self.contract.functions.retrieveLname().call()

    def getSalary(self):
        return self.contract.functions.retrieveSalary().call()


blockChain = blockChain()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/setEmployee/', methods=['GET', 'POST'])
def setEmployee():
    data = request.get_json()
    blockChain.setEmployee(data['firstName'], data['lastName'], data['salary'])
    return {
        'status': 'success',
        'message': 'Employee added successfully'
    }


@app.route('/getEmployee/', methods=['GET', 'POST'])
def getEmployee():
    return {
        'status': 'success',
        'message': blockChain.getEmployee()
    }


@app.route('/getFirstName/', methods=['GET', 'POST'])
def getFirstName():
    return {
        'status': 'success',
        'message': blockChain.getFirstName()
    }


@app.route('/getLastName/', methods=['GET', 'POST'])
def getLastName():
    return {
        'status': 'success',
        'message': blockChain.getLastName()
    }


@app.route('/getSalary/', methods=['GET', 'POST'])
def getSalary():
    return {
        'status': 'success',
        'message': blockChain.getSalary()
    }


if __name__ == '__main__':
    app.run(debug=True)
