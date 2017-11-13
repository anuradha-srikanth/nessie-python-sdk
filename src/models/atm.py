class ATM(object):

    # For the ATM class, I'm only creating an init from dict function because a user should never be able to create an atm object
    # The init function should only be called by the getAtms functions, so only initializing from dict is required
    def __init__(self, jsonData):
        self.atmId = jsonData.get('_id')
        self.name = jsonData.get('name')
        self.language_list = jsonData.get('language_list')
        self.address = jsonData.get('address')
        self.amount_left = jsonData.get('amount_left')
        self.accessibility = jsonData.get('accessibility')
        self.hours = jsonData.get('hours')
        self.geocode = jsonData.get('geocode')

    def toDict(self):
        returnDict = {}
        returnDict['_id'] = self.atmId
        returnDict['name'] = self.name
        returnDict['language_list'] = self.language_list
        returnDict['address'] = self.address
        returnDict['amount_left'] = self.amount_left
        returnDict['accessibility'] = self.accessibility
        returnDict['hours'] = self.hours
        returnDict['geocode'] = self.geocode
        return returnDict