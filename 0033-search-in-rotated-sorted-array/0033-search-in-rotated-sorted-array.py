class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set the initial indices
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # If left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # If right half is sorted
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If target is not found
        return -1
