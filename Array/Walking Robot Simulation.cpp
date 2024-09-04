// LC no 874
// Link: https://leetcode.com/problems/walking-robot-simulation/description/

// Time Complexity: O(m+n+s)
// m=no of obstacles,n=numbers of commands,s=no of steps ;

class Solution {
    bool x_plus=false,x_minus=false,y_plus=true,y_minus=false;
public:
    void changeDirOne()
    {
        if(y_plus==true)
        {
            y_plus=false;
            x_plus=true;
        }
        else if(x_plus)
        {
            x_plus=false;
            y_minus=true;
        }
        else if(y_minus)
        {
            x_minus=true;
            y_minus=false;
        }
        else{
            x_minus=false;
            y_plus=true;
        }
    }
    void changeDirTwo()
    {
        if(y_plus==true)
        {
            y_plus=false;
            x_minus=true;
        }
        else if(x_plus)
        {
            x_plus=false;
            y_plus=true;
        }
        else if(y_minus)
        {
            x_plus=true;
            y_minus=false;
        }
        else{
            x_minus=false;
            y_minus=true;
        }
    }
    int robotSim(vector<int>& c, vector<vector<int>>& o) {
        unordered_set<string>hash;
        int maxi=0;
        for(int i=0;i<o.size();i++)
        {
            string obs=to_string(o[i][0])+"+"+to_string(o[i][1]);
            hash.insert(obs);
        }
        int x=0,y=0;
        for(int i=0;i<c.size();i++)
        {
            if(c[i]==-1)
            {
                changeDirOne();

            }
            else if(c[i]==-2)
            {
                changeDirTwo();
            }
            else{
                if(x_minus)
                {
                    //x*=-1;
                    while(c[i]--)
                    {
                        x-=1;
                        string temp=to_string(x)+"+"+to_string(y);
                        if(hash.find(temp)!=hash.end())
                        {
                            x+=1;
                            break;
                        }
                    }

                    maxi=max(maxi,(x*x+y*y));
                }
                else if(y_minus)
                {
                    //y*=-1;
                    while(c[i]--)
                    {
                        y-=1;
                        string temp=to_string(x)+"+"+to_string(y);
                        if(hash.find(temp)!=hash.end())
                        {
                            y+=1;
                            break;
                        }
                    }
                    maxi=max(maxi,(x*x+y*y));
                }
                else if(y_plus)
                {
                    while(c[i]--)
                    {
                        y+=1;
                        string temp=to_string(x)+"+"+to_string(y);
                        if(hash.find(temp)!=hash.end())
                        {
                            y-=1;
                            break;
                        }
                    }
                    maxi=max(maxi,(x*x+y*y));
                }
                else if(x_plus)
                {
                    while(c[i]--)
                    {
                        x+=1;
                        
                        string temp=to_string(x)+"+"+to_string(y);
                        if(hash.find(temp)!=hash.end())
                        {
                            x-=1;
                            break;
                        }
                    }
                    cout<<x<<" "<<y;
                    maxi=max(maxi,(x*x+y*y));
                }
                
            }
        }

        return maxi;
    }
};
