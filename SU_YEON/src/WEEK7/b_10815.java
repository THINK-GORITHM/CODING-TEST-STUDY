package WEEK7;

import java.io.*;
import java.util.*;

public class b_10815 {
    static int N, M;
    public static void main(String[] arags) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        int[] s = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            s[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(s);

        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<M; i++){
            int temp = Integer.parseInt(st.nextToken());
            sb.append(check(s, temp)).append(" ");
        }
        System.out.println(sb);
    }

    static int check(int[] s, int temp){
        int start = 0;
        int end = N-1;
        int mid;

        while(start <= end){
            mid = (start + end) / 2;

                if(s[mid] == temp){
                    return 1;
                }else if(temp > s[mid]){
                    start = mid+1;
                }else{
                    end = mid-1;
                }
            }
        return 0;
    }
}
