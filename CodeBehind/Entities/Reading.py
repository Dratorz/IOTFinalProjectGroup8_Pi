class Reading:
    reading_id = 0
    rasp_id = ""
    value = 0.0
    type_id = 0
    unit_id = 0
    online = False
    
    def __init__(self, rasp_id: str, value: float, type_id: int, unit_id: int, online: bool=0):
        self.rasp_id = rasp_id
        self.value = value
        self.type_id = type_id
        self.unit_id = unit_id
        self.online = online
        
        