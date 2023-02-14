package WEEK6;

import java.io.*;
import java.util.StringTokenizer;

public class b_11724 {

    static int[][] graph;
    static int V;
    static boolean[] visited;

    public static void dfs(int index){
        if(visited[index] == true){
            return;
        }
        else{
            visited[index] = true;
            for(int i=1; i<=V; i++){
                if(graph[index][i] == 1){
                    dfs(i);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        graph = new int[V+1][V+1];
        visited = new boolean[V+1];

        for(int i=0; i<E; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x][y] = graph[y][x] = 1;
        }

        int count = 0;
        for(int i=1; i<=V; i++){
            if(visited[i] == false){
                dfs(i);
                count++;
            }
        }
        System.out.println(count);
    }
}
