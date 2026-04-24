class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        boats = 0

        while start <= end:
            # heaviest at limit → alone
            if people[end] == limit:
                boats += 1
                end -= 1
            # lightest at limit → alone
            elif people[start] == limit:
                boats += 1
                start += 1
            # try to pair
            elif people[start] + people[end] <= limit:
                boats += 1
                start += 1
                end -= 1
            # can't pair → heaviest alone
            else:
                boats += 1
                end -= 1

        return boats