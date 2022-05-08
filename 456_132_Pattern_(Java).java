class Solution {
    public boolean find132pattern(int[] nums) {        
        /*
        Search for a sequence s1, s2, s3 such that: s1 < s3 < s2 (SO S3 IS MAX)
        
        First find s2 (the largest), then s3, then s1
        */
        // edge case
        if(nums.length < 3) return false;
        
        Stack<Integer> stack = new Stack(); //we put the 32 of the pattern in here
        int num2 = Integer.MIN_VALUE;
        
        //check if the current number is less than num2. If it is, it means
        //our 132 pattern is satisfied, so return true
        for(int i=nums.length-1; i>=0; i--){
            if(nums[i] < num2)
                return true;
            
        //if the above is not true, update the peak value in the stack
        //keep popping from the stack until stack is empty
        //OR
        //the top value is greater than the current value
            while(!stack.isEmpty() && nums[i] > stack.peek()){
                num2 = stack.pop();
            }
        stack.push(nums[i]);
        }
        return false;
    }
}