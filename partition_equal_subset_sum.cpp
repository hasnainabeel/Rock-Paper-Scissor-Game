class Solution {
public:
    int dp[203][20010];
    bool func(int index,int target,vector<int> &v)
    {
        if(target==0)
            return true;
        if(index<0)
            return false;
        if(dp[index][target]!=-1)
            return dp[index][target];
        
        
bool isPossible=func(index-1,target,v);
        if(target>=v[index])
        isPossible|=func(index-1,target-v[index],v);
        return dp[index][target]=isPossible;
        
        
    }
    bool canPartition(vector<int>& nums) {
        memset(dp,-1,sizeof(dp));
        
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum%2!=0)
            return false;
        sum/=2;
        return func(nums.size()-1,sum,nums);
        
        
        
    }
};
