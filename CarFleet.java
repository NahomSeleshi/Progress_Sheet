class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i=0;i<position.length;i++){
            hm.put(position[i],speed[i]);
        }
        Arrays.sort(position);
        Stack<Double> monStack =  new Stack<>();
        double currentTime;
        double distance;
        for(int i=position.length-1;i>=0;i--){
            distance = target - position[i];
            currentTime = distance/hm.get(position[i]);
            if(monStack.empty()){
                monStack.push(currentTime);
                continue;
            }
            if(!monStack.empty() && currentTime>monStack.peek()){
                monStack.push(currentTime);
            }
        }
        return monStack.size();  
    }
}
