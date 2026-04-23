class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // store the count frequency table
        // use hashmap

        HashMap<Integer,Integer> map=new HashMap<>();

        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }

            ArrayList<Integer> [] arr=new ArrayList[nums.length+1];

        for(int item:map.keySet()){
            int value=map.get(item);

            if(arr[value]==null){
                arr[value]=new ArrayList<>();
            }
            arr[value].add(item);
        }
        
        // top k element which are towards the end of arr
        int[] ans=new int[k];
        int counter=0;

        for(int i=arr.length-1;i>=0 && counter<k;i--){
     

            if(arr[i]!=null){
                for(int num:arr[i]){
                    ans[counter]=num;
                    counter++;
                }
                if (counter == k) {
                        break;
                }
            }
           
        }

    return ans;
    }
}
