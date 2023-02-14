package WEEK6;

import java.io.*;
import java.util.*;

public class b_1260 {

    static int N, M, V;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        int[][] adjArray = new int[N+1][N+1];
        boolean[] visited_dfs = new boolean[N+1];
        boolean[] visited_bfs = new boolean[N+1];

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            adjArray[x][y] = 1;
            adjArray[y][x] = 1;
        }
        dfs(V, adjArray, visited_dfs);
        System.out.println();
        bfs(V, adjArray, visited_bfs);
    }

    public static void dfs(int V, int[][] adjArray, boolean[] visited){
        visited[V] = true;
        System.out.print(V + " ");

        for(int i=1; i<adjArray.length; i++){
            if(adjArray[V][i] == 1 && !visited[i]){
                dfs(i, adjArray, visited);
            }
        }
    }

    public static void bfs(int V, int[][] adjArray, boolean[] visited) {
        Queue<Integer> q = new ArrayDeque<>();

        q.offer(V);
        visited[V] = true;

        while (!q.isEmpty()) {
            V = q.poll();
            System.out.print(V + " ");

            for (int i = 1; i <= N; i++) {
                if (adjArray[V][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}
