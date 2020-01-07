class Plant:
    def __init__(self):
        self.up_speed = 0
        self.down_speed = 0
        self.desired_height = 0
        self.plant_height = 0
        self.count = 1
        self.days = 0

    def growing_plant(self, up_speed, down_speed, desired_height):
        self.plant_height = 0
        self.count = 1

        self._rules(up_speed, down_speed, desired_height)

        while self.plant_height < desired_height:
            if self.count % 2 == 1:
                self.plant_height += up_speed
            else:
                self.plant_height -= down_speed
            self.count += 1
        self.days = int(self.count / 2)
        return self.days

    def _rules(self, up_speed, down_speed, desired_height):
        if up_speed <= 5 or up_speed >= 100:
            raise Exception('UpSpeed must be between 5 and 100')
        if down_speed <= 2 or down_speed >= up_speed:
            raise Exception('DownSpeed must be between 2 and UpSpeed value')
        if desired_height <= 4 or desired_height >= 1000:
            raise Exception('DownSpeed must be between 4 and 1000')

plant = Plant()
plant.growing_plant(200, 10, 910)