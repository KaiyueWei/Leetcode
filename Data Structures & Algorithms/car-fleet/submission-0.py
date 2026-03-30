class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed_map = {}
        for i in range(len(position)):
            car_speed_map[position[i]] = speed[i]
        position.sort(reverse=True)
        fleet_count = 1
        current_fleet_finish_time = (target-position[0]) / car_speed_map[position[0]]
        for i in range(1, len(position)):
            finish_time = (target-position[i]) / car_speed_map[position[i]]
            if finish_time > current_fleet_finish_time:
                fleet_count += 1
                current_fleet_finish_time = finish_time
        return fleet_count


        