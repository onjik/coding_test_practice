package org.example.prog.괄호변환;

import java.util.Stack;
import java.util.StringTokenizer;
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.solution(")(");
        System.out.println(result);
    }
}



class Solution {

    private String swap(String p) {
        StringBuilder sb = new StringBuilder();
        for (char c : p.toCharArray()) {
            if (c == '(') {
                sb.append(")");
            } else {
                sb.append("(");
            }
        }
        return sb.toString();
    }

    private boolean isValid(String p) {
        Stack<Character> s = new Stack<>();
        for (Character c: p.toCharArray()){
            if (c.equals('(')) {
                s.push(c);
                continue;
            }
            // 닫는 괄호면 꺼내려고 시도, 없으면 false
            if (s.size() == 0){
                return false;
            }
            s.pop();
        }
        //여기까지 왔는데 스택이 비워지지 않았으면 false
        return s.size() == 0;
    }

    private String solve(String p) {
        // 1.
        if (p.length() == 0) return p;
        // 2. 균형잡힌 두 문자열로 나눈다.
        int balance = 0;
        int idx = -1;
        //초기값 넣기
        if (p.charAt(0) == '('){
            balance++;
        } else {
            balance--;
        }
        for (int i = 1; i < p.length(); i++){
            if (p.charAt(i) == '('){
                balance++;
            } else {
                balance--;
            }
            //균형이 맞았으면, idx 업데이트
            if (balance == 0){
                idx = i;
                break;
            }
        }
        String u = p.substring(0, idx + 1);
        String v = p.substring(idx + 1);

        if (isValid(u)){
            //3.
            return u + solve(v);
        } else {
            //4.
            StringBuilder sb = new StringBuilder();
            sb.append("(");
            sb.append(solve(v));
            sb.append(")");
            int l = u.length();
            String tmp = u.substring(1, l - 1);
            sb.append(swap(tmp));
            return sb.toString();
        }
    }

    public String solution(String p){
        return solve(p);
    }
}
