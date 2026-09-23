# https://www.hackerrank.com/challenges/ctci-ransom-note (example placeholder — swap for the real problem link)
#
# Given an array of integers and a target, return the indices of the two
# numbers that add up to the target.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
