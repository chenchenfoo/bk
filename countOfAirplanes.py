"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        length = len(airplanes)
        if length <= 1:
            return length
        max = airplanes[0].end
        for i in range(length):
            if airplanes[i].end > max:
                max = airplanes[i].end
        count = (max + 1) * [0]
        for i in range(length):
            count[airplanes[i].start] = count[airplanes[i].start] + 1
            count[airplanes[i].end] = count[airplanes[i].end] - 1
        res = 1
        t = 0
        for i in range(max):
            t = t + count[i]
            if t < 0:
                t = 0
            if t > res:
                res = t
        return res









if __name__ == "__main__":
    airplanes = [
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
    result = Solution().countOfAirplanes(airplanes)
    print result
