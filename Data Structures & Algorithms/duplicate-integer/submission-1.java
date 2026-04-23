class Solution {
    public boolean hasDuplicate(int[] nums) {

        // sort and check next index nlogn+O(N)

        // hashmap ) nlog(n)
        
          HashSet<Integer> seen = new HashSet<>();

        for(int i=0;i<nums.length;i++){
             if (seen.contains(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }

      return false;
    }
}
