class Transportation:
    def __init__(self, personid,serviceid, uses_in_morning,uses_in_evening,seat_nr,service_fee,stop_name):
        self.personid = personid
        self.serviceid = serviceid     
        self.uses_in_morning = uses_in_morning
        self.uses_in_evening = uses_in_evening
        self.seat_nr = seat_nr
        self.service_fee = service_fee
        self.stop_name = stop_name