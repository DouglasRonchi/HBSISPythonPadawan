
def growing_plant(up_speed, down_speed, desired_height):
    plant_height = 0
    count = 1

    if 5 >= up_speed >= 100:
        raise Exception('UpSpeed must be between 5 and 100')
    if 2 >= down_speed > up_speed:
        raise Exception('DownSpeed must be between 2 and UpSpeed value')
    if 4 >= desired_height >= 1000:
        raise Exception('DownSpeed must be between 4 and 1000')

    while plant_height < desired_height:
        if count % 2 == 1:
            plant_height += up_speed
        else:
            plant_height -= down_speed
        count += 1
    days = int(count / 2)
    return days
