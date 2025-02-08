/*
* Leetcode : 2349
* T.C : O(N) where N is container size
* S.C : O(N)+O(100000)
*/

// Using map with Priority_queue

class NumberContainers {
    unordered_map<int,int>mp; // Main number container
    unordered_map<int,priority_queue<int,vector<int>,greater<int>>>indices;
public:
    NumberContainers() {
        mp.reserve(100000);
    }
    
    void change(int index, int number) {
        mp[index]=number;
        indices[number].push(index);
    }
    
    int find(int number) {
        if (indices.find(number)==indices.end()){
            return -1;
        }
        while (!indices[number].empty()){
            int idx=indices[number].top();
            if (mp[idx]==number){
                return idx;
            }
            indices[number].pop();
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
