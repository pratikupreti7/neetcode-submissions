class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // first store the frquency map

        HashMap<Integer,Integer> map=new HashMap<>();

        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }

        // buckets needed to store the similar frequency items

        ArrayList<Integer>[] buckets=new ArrayList[nums.length+1];

        for(int item:map.keySet()){
            int value=map.get(item);
            if(buckets[value]==null){
                buckets[value]= new ArrayList<>();
            }
            buckets[value].add(item);
        }
        // storing the top k element
        int [] ans=new int[k];
        int count=0;

        for(int i=buckets.length-1;i>=0 && count<k;i--){
            
                if(buckets[i]!=null){
                    for(int num:buckets[i]){
                        ans[count] = num;
                        count++;
                    if (count == k) {
                        break;
                    }
                    }
                }
        
        
        }

        return ans;
    }
}
