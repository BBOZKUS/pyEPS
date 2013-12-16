def authenticationRequest(nasPd,spareHO,keyID,RAND,AUTN):
    return (
        "nas",
        {
         "messageType": {
          "procedureCode": "authRequest",
          "typeOfMessage": "initiatingMessage"
         },
         "spareHO":spareHO,
         "nasPd":nasPd,
         "keyID":keyID,
         "authenticationRAND":RAND,
         "authenticationAUTN":AUTN
        }
    )
            
def authenticationResponse(nasPd,RES):
    return (
        "nas",
        {
         "messageType": {
          "procedureCode": "authResponse",
          "typeOfMessage": "initiatingMessage"
         },
         "nasPd":nasPd,
         "authenticationResponse":RES,
        }
    )       