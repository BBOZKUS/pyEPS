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
         "RAND":RAND,
         "AUTN":AUTN,
        }
    )
            
def authenticationResponse(nasPd,RES):
    return (
        "nas",
        {
         "messageType": {
          "procedureCode": "authResponse",
          "typeOfMessage": "responseMessage"
         },
         "nasPd":nasPd,
         "authenticationResponse":RES,
        }
    )       