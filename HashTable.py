from typing import List

# x + y = z
# Loop through list
#   Add z - y = x to dict at index x
#   Check for x key in dict
#       Return [index x, index y]
#   Continue loop through at index y


def twoSum(nums: List[int], target: int) -> List[int]:
    table = {}
    i = 0
    while i < len(nums):
        x = target - nums[i]
        if x in table:
            return [table[x], i]
        table[nums[i]] = i
        i = i + 1
    return None


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))


if __name__ == "__main__":
    main()
