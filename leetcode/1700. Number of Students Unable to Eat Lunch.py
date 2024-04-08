from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cant = 0

        while len(sandwiches) > 0 and cant < len(students):
            s = students[0] # first student in line
            students.remove(s) # remove student [1], leave

            top = sandwiches[0] # [0], i won't pop for now

            if s == top:
                sandwiches.remove(top) # remove the sandwich, student is already left
                cant = 0
            else:
                students.append(s) # rejoin from behind
                cant += 1

        return len(students)

        
# other
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining
