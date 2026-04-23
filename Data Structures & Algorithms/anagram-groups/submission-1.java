class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> ans=new HashMap<>();
        // looping through all item 
        // each item needs to be converted to charArray and kept as a key in hasmap
        // if key exist then add the item to list
        // if it doesnot then add to new list

        // for n* (m)

        for(String str: strs){
            // store in charArr
            int charArr[]=new int[26];
            for(int i=0;i<str.length();i++){
                charArr[str.charAt(i)-'a']++;
            }
            // store the key convert the arr to string

            String key= Arrays.toString(charArr);

            if(!ans.containsKey(key)){
                 ans.put(key, new ArrayList<>());
            }
             ans.get(key).add(str);
        }


        return new ArrayList<>(ans.values());

        
    }
}
