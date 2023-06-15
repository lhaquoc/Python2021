def count_occurrence(nums, x):
  count = 0
  for item in nums:
    if x == item:
      count += 1 # count = count + 1

  return count

def sum_nums(nums):
  res = 0
  for item in nums:
    res += item # res = res + item
  if res > 0:
    return res / len(nums)
  return 0

nums = [1,2,3,4,5,6,6,6,5]
x = 6
print(count_occurrence(nums, x))


res = [item for item in nums if item > 0]
print(res)
