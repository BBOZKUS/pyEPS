import random
from eps.messages.nas import authenticationRequest

class nasAuthenticationRequestProcedureHandler(object):
    def __init__(self,procedureParameters,ueAddress,ioService):
        self.procedureParameters = procedureParameters
        self.ueAddress = ueAddress
        self.ioService = ioService
    
    def execute(self):
        if self.checkParameters() == 0 :
            raise Exception("Missing Nas Authentication Request Parameters")
        else :
            self.sendAuthenticationRequestMessage()

    def sendAuthenticationRequestMessage(self):
        parameters = (
                      self.procedureParameters["nasPd"],
                      self.procedureParameters["spareHO"],
                      self.procedureParameters["keyID"],
                      self.procedureParameters["AUTN"],
                      self.generateRAND()
                      )
        self.ioService.sendMessage(self.ueAddress, *authenticationRequest(*parameters))
        
    def checkParameters(self):
        requiredProcedureParameters = ("spareHO","nasPd","keyID","AUTN")
        missingParameters = set(requiredProcedureParameters) - set(self.procedureParameters)
        if missingParameters:
            return 0
        else:
            return 1
        
    def generateRAND(self):
        return random.randint(0,127);
    
    
    
    
    