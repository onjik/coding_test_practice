package org.example;// 단순 정렬하라는 문제인듯
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] result = sol.solution(4, new int[]{4,4,4,4,4});
        for (int r : result){
            System.out.println(r);
        }

    }
}
class Solution {
    public int[] solution(int N, int[] stages) {

        Stage[] infos = new Stage[N];
        // 초기화
        for (int i = 0; i < N; i++){
            infos[i] = new Stage(i + 1);
        }

        // 그리고 stage마다 적용한다.
        for (int s : stages){
            for (int j = 0; j < s -1; j++) {
                Stage cur = infos[j];
                cur.reached += 1;
            }
            if (s -1 >= N) continue;
            infos[s -1].reached += 1;
            infos[s -1].stopped += 1;
        }

        return Arrays.stream(infos).sorted().mapToInt(s -> s.no).toArray();
    }

    static class Stage implements Comparable<Stage> {
        int no;
        int reached;
        int stopped;
        public Stage(int no){
            this.no = no;
            this.reached = 0;
            this.stopped = 0;
        }


        public int compareTo(Stage s){
            int a = this.stopped * s.reached;
            int b = s.stopped * this.reached;
            if (a == b){
                return this.no - s.no; // 오름 차순
            }
            return b - a; // 내림차순
        }
    }
}