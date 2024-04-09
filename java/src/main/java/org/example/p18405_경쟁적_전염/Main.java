package org.example.p18405_경쟁적_전염;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// N *N 크기 시험관
// 바이러스 종류 1~K
// 1초마다 상하좌우로 증식
// 번호 낮은거부터 우선 증식
// S초 후 x,y에 존재하는 바이러스 종류 출력

//전형적인 bfs 문제
// 다만 번호가 낮은거 부터 움직여야 한다.
import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};
    static int n;
    static int[][] board;
    public static void main(String args[]) throws Exception{
        //input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        var tk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(tk.nextToken());
        int k = Integer.parseInt(tk.nextToken());
        // 맵을 입력받는다.
        board = new int[n][n];
        for (int y = 0; y < n; y++){
            var tok = new StringTokenizer(br.readLine());
            for (int x = 0; x < n; x++){
                board[y][x] = Integer.parseInt(tok.nextToken());
            }
        }
        // 메타 정보를 입력 받는다
        tk = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(tk.nextToken());
        int x = Integer.parseInt(tk.nextToken()); // 이게 행
        int y = Integer.parseInt(tk.nextToken()); // 이게 열
        //bfs 돌린다.
        bfs(s);
        // 그리고 해당 위치에서 값을 읽어서 출력한다.
        System.out.println(board[x-1][y-1]);

    }
    public static void bfs(int step){
        //우선순위 큐인데, 해당 위치의 값을 기준으로 작은거 부터
        LinkedList<Point> q = new LinkedList<>();
        // 초기값 설정 - 다 돌면서 값이 0이 아닌 곳을 전부 추가
        for (int y = 0; y < n; y++){
            for (int x = 0; x < n; x++){
                if (board[y][x] != 0){
                    q.offer(new Point(x,y));
                }
            }
        }


        // 그다음 이것을 가지고 bfs를 돌린다.
        while (step > 0){
            // 같은 거리는 다 돌린다.
            int len = q.size();
            q.sort((a,b) -> a.getValue() - b.getValue());
            for (int i = 0; i < len; i ++){
                Point now = q.poll();
                int x = now.x;
                int y = now.y;
                for (int j = 0; j < 4;j++){
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    //맵 밖에 나갔나 체크하기
                    if (nx < 0 || nx >= n || ny < 0|| ny >= n) continue;
                    // 이미 방문된 장소인지 체큿하기
                    if (board[ny][nx] != 0) continue;
                    // 방문 처리하기
                    board[ny][nx] = board[y][x];
                    q.offer(new Point(nx,ny));
                }
            }
            step--;
        }


    }

    public static class Point {
        int x;
        int y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public int getValue(){
            return board[y][x];
        }
    }

}