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

        print(values)

        for i in range(len(values) - 1, -1, -1):
            if values[i][1] <= timestamp:
                return values[i][0]

        return ""
            
