class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // store count of each element in count++
        HashMap<Integer,Integer> map=new HashMap<>();

       for(int num:nums){
        map.put(num,map.getOrDefault(num,0)+1);
       }
        // 1,2,3,4,5,6
        ArrayList<Integer>[] bucket=new ArrayList[nums.length+1];
       for(int key:map.keySet()){
        int position=map.get(key);
        if(bucket[position]==null){
            bucket[position]=new ArrayList<>();
        }
        bucket[position].add(key);
       }

    //    storing the result

    int[] ans=new int[k];
    int count=0;

          // Start from the highest possible frequency and add elements to the result
        for (int i = bucket.length - 1; i >= 0 && count < k; i--) {
            if (bucket[i] != null) {
                for (int num : bucket[i]) {
                    ans[count++] = num;
                    if (count == k) {
                        break;
                    }
                }
            }
        }

        return ans;
    }
}
