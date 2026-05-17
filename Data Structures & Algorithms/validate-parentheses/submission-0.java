class Solution {

    public boolean isValid(String s) {
        Stack<Character> characters = new Stack<>();
        char check = ' ';
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '{' || c == '(' || c == '[') {
                characters.push(c);
            } 
            else if (c == '}' || c == ']' || c == ')') {
                if (characters.isEmpty()) return false;

                if (c == '}' || c == ']' || c == ')') {
                check = characters.pop();
                }
                if (c == '}' && check != '{') {
                    return false;
                }
                if (c == ']' && check != '[') {
                    return false;
                }
                if (c == ')' && check != '(') {
                    return false;
                }
            }
        } 

        return characters.isEmpty();
        }

}
    
    