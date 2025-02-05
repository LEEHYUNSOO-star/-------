class Athlete:
    def __init__(self, name, sport, record): # 선수 이름, 종목, 기록 초기화화
        self.name = name
        self.sport = sport  
        self.record = record
        
    def update_record(self, new_record): #기록 업데이트 메서드드
        self.record = new_record
        print(f"{self.name}의 new record : {self.record}")
        
    def display_info(self):
        print(f"이름: {self.name}, 종목: {self.sport}, 기록: {self.record}")