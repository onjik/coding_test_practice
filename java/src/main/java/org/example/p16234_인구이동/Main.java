package org.example.p16234_인구이동;
// 1 -> k -> x
// 최소 시간 구해라

// 최단 거리 문제

// N , M < 100
// 500 이하이므로, 워셜 플로이드 쓰자

import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int l;
    static int r;
    static int[][] board;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static boolean[][] visited;
    public static void main(String args[]) throws Exception{
        var br = new BufferedReader(new InputStreamReader(System.in));
        var tk = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(tk.nextToken());
        l = Integer.parseInt(tk.nextToken());
        r = Integer.parseInt(tk.nextToken());
        // 맵 초기화
        board = new int[n][n];
        visited = new boolean[n][n];
        for (int y = 0; y < n; y++){
            tk = new StringTokenizer(br.readLine(), " ");
            for (int x = 0; x < n; x++){
                board[y][x] = Integer.parseInt(tk.nextToken());
            }
        }
        // 이제 쭉 돌면서 bfs를 다 호출한다.
        boolean changed = true;
        int dayCount = 0;
        while (changed){
            changed = false;
            for (int y = 0; y < n; y++){
                for (int x = 0; x < n; x++){
                    visited[y][x] = false;
                }
            }
            for (int y = 0; y < n; y++){
                for (int x = 0; x < n; x++){
                    changed = bfs(x,y) || changed;
                }
            }
            if (changed) dayCount += 1; // 여기 틀렸었음 - changed가 true일때만 증가해야함
        }

        System.out.println(dayCount);
    }

    static boolean bfs(int x, int y){
        if (visited[y][x]) return false;
        List<Point> q = new ArrayList<>();
        // 초기값 집어넣기
        q.add(new Point(x,y));
        visited[y][x] = true;

        // 인덱스 포인터
        int idx = 0;
        int sum = 0;

        while (q.size() - 1 >= idx){
            Point cur = q.get(idx++);
            sum += board[cur.y][cur.x];
            // 이웃 탐색
            for (int i = 0; i < 4;i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                int diff = Math.abs(board[cur.y][cur.x] - board[ny][nx]); // 여기 틀렷었음 - cur.x 대신 x 써서
                if (!(diff <= r && diff >= l)) continue;
                if (visited[ny][nx]) continue;
                visited[ny][nx] = true;
                q.add(new Point(nx,ny));
            }
        }
        if (q.size() == 1) return false;
        // 그다음 그룹을 갱신한다.
        int v = sum / q.size();
        for (Point p : q){
            board[p.y][p.x] = v;
        }
        return true;
    }

    static class Point {
        int x;
        int y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
}