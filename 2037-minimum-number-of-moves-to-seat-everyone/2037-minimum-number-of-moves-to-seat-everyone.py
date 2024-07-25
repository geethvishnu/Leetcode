class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        r=0
        for i in range(len(seats)):
            r+=abs(students[i]-seats[i]) 
        return r