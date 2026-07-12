'''
U
[1,2,4,5]
[1,2,2,3,3]
 l       r
-people[i] is the weight of the ith person
Constraints:
    -infinite number of boats
    -Max weight of limit
    -at most 2 people per boat
Edge case:
    -no people/people is empty

    [2,2,4,5], l = 6
     l   r

    [1,2,2,3,3]
     l   r
    []
M
-Two pointers
P
-if not people return 0
-sort people
-initilaize l, r = 0, len - 1
-initialize count
-while l <= r:
    -while people[r] == limit:
        -if people[l] < people[r]:
            -increment count
            -decrement r
        -elif people[l] == people[r]:
            -increment count
            -decrement r
            -continue
    -while people[l] == limit:
        -increment count
        -increment l
    -total = people[l] + people[r]
    -if total == limit:
        -increment count
        -increment l
        -decrement r
    -if total > limit:
        -increment count
        -decrement r
    -elif total < limit:
        -increment count
        -increment l

return count
IRE
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            '''while people[r] == limit:
                if people[l] < people[r]:
                    count += 1
                    r -= 1
                elif people[l] == people[r]:
                    count += 1
                    r -= 1
                    continue
            while people[l] == limit:
                if people[l] < people[r]:
                    count += 1
                    l += 1
                elif people[l] == people[r]:
                    count += 1
                    l += 1
                    continue
            total = people[l] + people[r]
            if total == limit:
                count += 1
                l += 1
                r -= 1
            elif total > limit:
                count += 1
                r -= 1
            elif total < limit:
                count += 1
                l += 1'''
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            count += 1
        return count