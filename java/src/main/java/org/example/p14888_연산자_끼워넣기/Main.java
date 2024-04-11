package org.example.p14888_연산자_끼워넣기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


// 연산자 배치해서, 나올 수 있는 결과의 최소와 최대 값을 구하라
// N < 11
// 굉장히 작다 그냥 완전 탐색 해도 될듯
import java.util.*;
import java.util.stream.*;
import java.util.function.*;
import java.io.*;

public class Main {
    static int n;
    static int[] arr;
    static int[] oper; // +-*/
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    private static int calculate(int idx, int value, int operIdx){
        Function<Integer,Integer> fun;
        if (operIdx == 0){
            fun = (i) -> value + arr[i + 1];
        } else if (operIdx == 1){
            fun = (i) -> value - arr[i + 1];
        } else if (operIdx == 2) {
            fun = (i) -> value * arr[i + 1];
        } else {
            fun = (i) -> value / arr[i + 1];
        }
        return fun.apply(idx);
    }


    /**
     * @param idx 0부터 시작하는 오퍼레이션 위치
     */
    private static void dfs(int idx,int value){
        // 맨 마지막을 넘어서면 끝낸다.
        if (idx >= n -1) {
            max = Math.max(max, value);
            min = Math.min(min, value);
            return;
        }
        // 각 오퍼레이션을 돌아가면서 사용
        for (int i = 0; i < 4; i++){
            if (oper[i] == 0) continue;
            oper[i] -= 1;
            dfs(idx + 1, calculate(idx,value, i));
            oper[i] += 1;
        }
    }


    public static void main(String args[]) throws Exception {
        //input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        var tk = new StringTokenizer(br.readLine(), " ");
        int cnt = tk.countTokens();
        arr = new int[cnt];
        for (int i = 0; i < cnt; i++){
            arr[i] = Integer.parseInt(tk.nextToken());
        }
        tk = new StringTokenizer(br.readLine(), " ");
        oper = new int[4];
        for (int i = 0; i < 4;i++){
            oper[i] = Integer.parseInt(tk.nextToken());
        }

        // 이제 탐색을 시작한다.
        dfs(0,arr[0]);

        System.out.println(max);
        System.out.println(min);




    }
}