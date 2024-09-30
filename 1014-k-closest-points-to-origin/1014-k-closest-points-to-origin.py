class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        for i in range(len(points)):
            dist = (((points[i][0]) ** 2) + ((points[i][1]) ** 2)) ** 0.5
            distances.append([dist, i])
        distances.sort()
        return [points[distances[i][1]] for i in range(len(distances)) if i < k]
        