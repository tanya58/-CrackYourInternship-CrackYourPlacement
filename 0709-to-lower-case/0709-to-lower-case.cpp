class Solution {
public:
    string toLowerCase(string s) {
        int n=s.length();

       for(int i=0; i<n; i++)
       {
            if(toupper(s[i]))
            s[i]=tolower(s[i]);
       } 
       return (s);
    }
};