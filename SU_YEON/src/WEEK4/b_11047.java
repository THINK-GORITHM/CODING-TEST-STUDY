package WEEK4;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class b_11047 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayList<Integer> coins = new ArrayList();
        int cnt = 0;

        for(int i=0; i<N; i++) {
            coins.add(Integer.parseInt(br.readLine()));
        }

        for(int j=N-1; j>=0; j--){
            if(K/coins.get(j) != 0){
                cnt += K/coins.get(j);
                K = K % coins.get(j);
            }
        }

        System.out.println(cnt);
    }
}
