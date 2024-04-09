package org.example.prog.연구소;

// 매우 범위가 적으므로 완전 탐색
// dfs로 벽을 채우고, bfs로 바이러스를 퍼트리자
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Main {

    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int[][] originalMap;
    static int maxSafezone = 0;
    static int n;
    static int m;

    public static void main(String[] args) throws Exception{



        // Stream - String 역순
        String str = "hello";
        String reversed = new StringBuilder(str).reverse().toString();



        // 입력 받기
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());
        originalMap = new int[n][m];
        for (int y = 0; y < n; y++ ){
            var tk = new StringTokenizer(reader.readLine());
            for (int x = 0; x < m; x++){
                originalMap[y][x] = Integer.parseInt(tk.nextToken());
            }
        }
        dfs(0);
        System.out.println(maxSafezone);
    }

    public static void dfs(int wallCount){
        // 3개가 선택되었으면 바이러스 퍼트린다.
        if (wallCount == 3){
            bfs();
            return;
        }
        for (int y = 0;y < n;y++){
            for (int x = 0; x < m; x++){
                if (originalMap[y][x] == 0) {
                    originalMap[y][x] = 1;
                    dfs(wallCount + 1);
                    originalMap[y][x] = 0;
                }
            }
        }
    }
    // 현재 지도에서 바이러스를 퍼트리고, 안전 지대를 갱신한다.
    public static void bfs() {
        Queue<Point> q = new LinkedList<>();

        // 2인 지점을 모두 집어 넣는다.
        for (int y = 0;y < n;y++){
            for (int x = 0; x < m; x++){
                if (originalMap[y][x] == 2){
                    q.add(new Point(x,y));
                }
            }
        }
        //원본 배열을 바꾸지 않기 위한 copyMap
        int[][] copy = new int[n][m];
        for (int i = 0; i < n;i++){
            copy[i] = originalMap[i].clone();
        }

        while (!q.isEmpty()){
            Point now = q.poll();
            int x = now.x;
            int y = now.y;
            // 주변을 둘러본다.
            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 맵 체크
                if ((nx < 0 || nx >= m) || (ny < 0 || ny >= n)) continue;
                // 빈칸이라면, 채워 넣고, 큐에 넣기
                if (copy[ny][nx] == 0){
                    copy[ny][nx] = 2;
                    q.add(new Point(nx,ny));
                }
            }
        }

        //그다음 빈칸 계산하기
        int count = safeZone(copy);
        maxSafezone = Math.max(count, maxSafezone);
    }

    public static int safeZone(int[][] copy){
        int count =0;
        for (int x = 0; x < m;x++){
            for (int y = 0; y < n;y++){
                if (copy[y][x] == 0){
                    count++;
                }
            }
        }
        return count;
    }


    public static class Point{
        int x;
        int y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        public int maxSafezone(){
            return maxSafezone;
        }
    }
}
