package WEEK4;

import java.io.*;
import java.util.*;

public class b_1449 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];

        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int count = 1;
        int idx = 0;

        for(int j=idx; j<N; j++){
            if(arr[idx]+L-1 < arr[j]){
                count++;
                idx=j;
            }
        }
        System.out.println(count);
    }
}
