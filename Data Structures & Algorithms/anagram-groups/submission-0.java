class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        // for each array item i can sort them and compare key and put the item

        HashMap<String,List<String>> ans=new HashMap<>();
      
        for(String ch:strs){
            int[] charArr=new int[26];
            // sort them or else I can also have them stored in char arr
           for (char c : ch.toCharArray()) {
                charArr[c - 'a']++;
            }
            String key=Arrays.toString(charArr);
            if (!ans.containsKey(key)) {
                ans.put(key, new ArrayList<>());
            }
            ans.get(key).add(ch);
        }
         return new ArrayList<>(ans.values());
    }
}
