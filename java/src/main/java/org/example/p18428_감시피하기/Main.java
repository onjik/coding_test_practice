package org.example.p18428_감시피하기;

// N * N 체스판
// 선생님T 학생S 장애물O
// 선생님 상하좌우 직선 감시가능
// 장애물에 가려짐

// 3개의 장애물 설치
// 모든 학생 살아 남도록

// 가능하면 "YES" 불가능하면 "NO"

// N < 6
// T < 5
// S < 30

// 3P36 *

// 범위가 굉장히 작네, 완전 탐색으로 단순 무식하게 가자
import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static char[][] board;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String args[]) throws Exception{
        var br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        StringTokenizer tk;
        for (int y = 0;y < n;y++){
            tk = new StringTokenizer(br.readLine(), " ");
            for (int x = 0; x < n;x++){
                board[y][x] = tk.nextToken().charAt(0);
            }
        }
        // 완전 탐색
        boolean result = dfs(0, 0);
        System.out.println(result ? "YES" : "NO");

    }

    // 여기서는 각 칸에 장애물을 배치한다.
    static boolean dfs(int idx, int count){
        if (count == 3){
            // 올바른지 체크한다.
            return isValid();
        }
        if (idx >= n * n) {
            // 3개가 안된체 마지막까지 온 경우
            return false;
        }

        boolean success = false;

        // 선택 하는 경우
        int x = idx % n;
        int y = idx / n;
        if (board[y][x] == 'X'){
            board[y][x] = 'O';
            success = dfs(idx + 1, count +1);
            if (success) {
                return success;
            }
            board[y][x] = 'X';
        }

        // 선택 안하는 경우
        return dfs(idx + 1, count);
    }

    static boolean isValid(){
        // 선생님의 수가 더 적으므로, 선생님 당으로 체크한다.
        for (int y = 0; y < n; y++){
            for (int x = 0; x < n;x++){
                if (board[y][x] != 'T') continue;
                for (int i = 0; i < 4; i++){
                    int nx = x;
                    int ny = y;
                    while(board[ny][nx] != 'O') {
                        nx += dx[i];
                        ny += dy[i];
                        if (nx >= n || nx < 0 || ny >= n || ny < 0) break;
                        // 이 칸이 사람이면, false
                        if (board[ny][nx] == 'S'){
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
