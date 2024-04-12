package org.example.p2110_공유기설치;
// 이진 탐색으로 해결해야한다.
// 파라 메트릭 서치
// 두 지점 사이의 거리를 이진 탐색으로 늘리고 줄이면서,
// C 값을 만족하는 최대 거리를 찾는다.
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception{
        var br = new BufferedReader(new InputStreamReader(System.in));
        var tk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(tk.nextToken());
        int c = Integer.parseInt(tk.nextToken());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        // sort - 오름 차순
        Arrays.sort(arr);

        // 그다음 최대 최소 거리를 구한다.
        int maxGap = arr[n-1] - arr[0];
        int minGap = 1;
        // 그다음 허용되는 한 최대 거리를 이진 탐색한다.
        int start = minGap;
        int end = maxGap;
        int result = 0;
        while(start <= end){ // start가 end랑 같더라도 돌아야함
            int mid = (start + end) / 2; // 현재 체크할 간격
            // 앞에서 부터 쭉 가면서 대입 해본다.
            int value = arr[0];
            int count = 1;
            for (int i = 1; i < n; i++){
                if (arr[i] >= value + mid){
                    count += 1;
                    value = arr[i];
                }
            }
            // 이제 잘 세어 졌는지 확인
            if (count >= c) {
                //현재까지 최적의 결과 저장
                result = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(result);

    }

}