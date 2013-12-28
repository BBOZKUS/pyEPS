from eps.messages.nas import authenticationResponse

class nasAuthenticationResponseProcedureHandler(object):
    def __init__(self,procedureParameters,mmeAddress,ioService):
        self.procedureParameters = procedureParameters
        self.mmeAddress = mmeAddress
        self.ioService = ioService
    
    def execute(self):
        if self.checkParameters() == 0 :
            raise Exception("Missisng Nas Authentication Response Parameters")
        else:
            self.sendAuthenticationResponseMessage();


    def sendAuthenticationResponseMessage(self):
        parameters = (
                      self.procedureParameters["nasPd"],
                      self.procedureParameters["RES"]
                     )
        self.ioService.sendMessage(self.mmeAddress,*authenticationResponse(*parameters))

    def checkParameters(self):
        requiredProcedureParameters = ("nasPd","RES")
        missingParameters = set(requiredProcedureParameters) - set(self.procedureParameters)
        if missingParameters:
            return 0
        else:
            return 1