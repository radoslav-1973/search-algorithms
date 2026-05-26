# The Boyer-Moore Voting Algorithm is a highly efficient algorithm used to find the majority element in a sequence—an element that appears more than times—in time and space. It uses a clever "cancellation" technique to track a candidate and a counter.
# test
# How it works:

# 1. We start with a candidate (initially None) and a count (initially 0)
# 2. When we see a new element:
      # If our count is 0, we pick this element as our new candidate
      # If this element matches our candidate, we increment the count
      # If this element is different from our candidate, we decrement the count

# Think of the count as keeping track of the “net votes” for our current candidate. When the count reaches zero, it means our current candidate has been “eliminated” by equal opposition.

def find_majority(nums):
    candidate = None
    count = 0
    
    # First pass: find a candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate
