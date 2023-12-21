package org.example.p2529_부등호;

import java.io.*;
import java.util.*;



public class Main {
    static boolean[] numbers;
    static int[] values;
    static char[] opers;
    static int count;
    static String max;
    static String min;


    public static void main(String args[]) throws Exception{

        //input
        var reader = new BufferedReader(new InputStreamReader(System.in));
        count = Integer.parseInt(reader.readLine());
        String s = reader.readLine();

        //init
        numbers = new boolean[10];
        values = new int[count+1];
        opers = new char[count+1];

        var tokenizer = new StringTokenizer(s, " ");
        int charIdx = 1;
        while (tokenizer.hasMoreTokens()){
            opers[charIdx++] = tokenizer.nextToken().charAt(0);
        }


        //call
        for (int i = 0; i < 10; i++){
            values[0] = i;
            numbers[i] = true;
            tracking(1);
            numbers[i] = false;
        }

        System.out.println(max);
        System.out.println(min);

    }

    private static void tracking(int idx){
        //종료 조건
        if (idx == count +1) {
            //여기까지 오면 성공한 것임
            var buffer = new StringBuffer();
            for (int i = 0; i < values.length; i++){
                buffer.append(values[i]);
            }

            if (min == null){
                min = buffer.toString();
            } else {
                max = buffer.toString();
            }

            return;
        }

        int prev = values[idx -1];
        char oper = opers[idx];

        for (int i = 0; i < 10; i++){
            if (numbers[i] == true) continue;
            if ((oper == '<' && prev < i) || oper == '>' && prev > i) {
                values[idx] = i;
                numbers[i] = true;
                tracking(idx+1);
                values[idx] = -1;
                numbers[i] = false;
            }
        }

    }
}