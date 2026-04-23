class Solution {
    public boolean isAnagram(String s, String t) {

        // sort string and compare each char 

        //  convert of hash and increase and descrease the counter

        // if both the string are equal or not

        if(s.length()!=t.length()){
            return false;
        }

        int[] charArr=new int[26];
        for(int i=0;i<s.length();i++){
            charArr[s.charAt(i)-'a']++;
            charArr[t.charAt(i)-'a']--;
        }

        for(int count : charArr){
            if(count!=0){
            return false;
            }
        }

        return true;

    }
}
