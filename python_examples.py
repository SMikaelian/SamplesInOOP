class Aircraft:
    #class attribute
    kind= 'flying aircraft'

    #initializer/instnace attribute
    def __init__(self, name, model, category, travelRate, manufacturingDate, status):
        self.name= name
        self.model= model
        self.category= category
        self.travelRate= travelRate
        self.manufacturingDate= manufacturingDate
        self.status= status

    #instance methods
    def props(self):
        return "{} is a {} {} and is {}.".format(a.name, a.category, a.kind, a.status)

    def get_name(self):
        return self._name

    def get_model(self):
        return self._model

    def get_category(self):
        return self._category

    def get_travelRate(self):
        return self._travelRate

    def get_manufacturingDate(self):
        return self._manufacturingDate

    def get_status(self):
        return self._status


#instantiate Aircraft object
a= Aircraft('Lockheed Martin F-35 Lightning II', 'F-35', 'air superiority, strike', 'supersonic', 'AUG 2016', 'In-service')
b= Aircraft('General Dynamics F-16 Fighting Falcon', 'F-16', 'air superiority', 'supersonic', 'JUN 2011', 'In-service')
c= Aircraft('Lockheed Martin F-22 Raptor', 'F-22', 'air superiority, ground attack, electronic warfare', 'supersonic', 'SEP 2012', 'In-service')

#access the instance attributes
print("{} is a {} {} and is {}.".format(a.name, a.category, a.kind, a.status))

#calling instance methods
print(a.props())
print(b.get_travelRate())
