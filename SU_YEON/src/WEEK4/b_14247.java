package WEEK4;

import java.io.*;
import java.util.*;

public class b_14247 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int sum = 0;

        for(int i=0; i<n; i++){
            sum+=Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] tree = new int[n];

        for(int i=0; i<n; i++){
            tree[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(tree);

        for(int i=0; i<n; i++){
            sum += tree[i] * i;
        }

        System.out.println(sum);

    }
}
