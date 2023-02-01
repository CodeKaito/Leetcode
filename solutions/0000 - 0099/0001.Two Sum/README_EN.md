# [1. Two Sum](https://leetcode.com/problems/two-sum)

## Description

<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code>O(n<sup>2</sup>)&nbsp;</code>time complexity?

## Solutions

<!-- tabs:start -->

### **Python3**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            x = target - v
            if x in m:
                return [m[x], i]
            m[v] = i
```

### **Java**

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            int v = nums[i];
            int x = target - v;
            if (m.containsKey(x)) {
                return new int[] {m.get(x), i};
            }
            m.put(v, i);
        }
        return null;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            int v = nums[i];
            int x = target - v;
            if (m.count(x)) return {m[x], i};
            m[v] = i;
        }
        return {};
    }
};
```

### **C#**

```cs
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var m = new Dictionary<int, int>();
        for (var i = 0; i < nums.Length; ++i)
        {
            int j;
            int v = nums[i];
            int x = target - v;
            if (m.TryGetValue(x, out j))
            {
                return new [] {j, i};
            }
            if (!m.ContainsKey(v))
            {
                m.Add(v, i);
            }

        }
        return null;
    }
}
```

### **JavaScript**

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const m = new Map();
    for (let i = 0; i < nums.length; ++i) {
        const v = nums[i];
        const x = target - v;
        if (m.has(x)) {
            return [m.get(x), i];
        }
        m.set(v, i);
    }
    return [];
};
```

<!-- tabs:end -->
