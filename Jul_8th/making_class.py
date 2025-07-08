class Car():
    total_num = 0    # class variable

    def __init__(self,
                 car_type: str,
                 car_volume: int, 
                 made_in_korea: bool, 
                 car_color: list[str]
                 ):
        self.car_type = car_type
        self.car_volume = car_volume
        self.made_in_korea = made_in_korea
        self.car_color = car_color

        Car.total_num = Car.total_num + 1


    def __getattribute__(self, name):
        return super().__getattribute__(name)

    
    @classmethod
    def get_num(cls):
        print(f"So far, {Car.total_num} car(s)")

    def info(self):
        print(f'차종 : {self.car_type}')
        print(f'배기량 : {self.car_volume}')
        print(f'국산차여부 : {self.made_in_korea}')
        print(f'희망색깔 : {self.car_color}')
    
    def check(self):
        print("Need car inspection")


if __name__ == "__main__":
    Car.total_num = 0

    morning1 = Car(car_type='Morning',
                car_volume=100,
                made_in_korea=True,
                car_color=['black', 'white', 'blue'])

    Lambo = Car(car_type='Lamborghini',
                car_volume=200,
                made_in_korea=False,
                car_color=['yes'])
    
    Car.get_num()