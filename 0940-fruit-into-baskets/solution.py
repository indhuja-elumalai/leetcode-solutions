
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, left, max_fruits = {}, 0, 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    keys = list(count.keys())  # Get keys manually
                    for key in keys:
                        if count[key] == 0:
                            count.pop(key)  # Remove empty fruit type
                            break
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits

