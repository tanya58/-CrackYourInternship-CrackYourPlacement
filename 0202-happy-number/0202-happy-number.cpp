class Solution {
public:
    bool isHappy(int n) {
       int added = n;
        int temp;
        int runc = 0;
        while(added != 1)
        {
            //std::cout << "new for loop with "<< added <<"\n"; 
            std::string numbers = std::to_string(added);
            added = 0;
            for(int i = 0; i < numbers.size(); ++i)
            {
                
                char tmps = numbers[i];
                temp = (int)tmps-48;
                temp*=temp;
                added +=temp;
                //std::cout << "added: " << added << "\n";

            }
            runc++;

            if(runc == 15)
            {
                return false;                
            }
            
        }

        if(added == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};