class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    # prev_timestamp <= timestamp
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key)

        if not values:
            return ""

        l, r = 0, len(values) - 1
        target = timestamp
        
        mid = (l + r) // 2
        while l <= r:
            if values[mid][1] == target:
                return values[mid][0]
            elif values[mid][1] < target:
                l = mid + 1
            else:
                r = mid - 1

            mid = (l + r) // 2
        
        if values[mid][1] <= timestamp:
            return values[mid][0]
        else:
            if mid - 1 >= 0:
                return values[mid - 1][0]
            return ""