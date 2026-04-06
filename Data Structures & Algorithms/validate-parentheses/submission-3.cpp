class Solution {
public:
    bool isValid(string s) {
        stack<char> pilha;

        int s_len = s.length();

        for(int i = 0; i < s_len; i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                pilha.push(s[i]);
            }

            else {
                // quer dizer que comecou com um fechado ... (errado)
                if(pilha.empty()) {
                    return false;
                }

                char top_elem = pilha.top();
                
                if(top_elem == '(' && s[i] == ')') {
                    pilha.pop();
                }
                
                else if(top_elem == '{' && s[i] == '}') {
                    pilha.pop();
                }
                
                else if(top_elem == '[' && s[i] == ']') {
                    pilha.pop();
                } 

                else {
                    return false;
                }   
            }
        }

        if(!pilha.empty()) {
            return false;
        }

        /* LINEAR */
        return true;   
    }
};
