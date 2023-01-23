package WEEK2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_2164 {

    public static void main(String[] arags) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] q= new int[2 * N];

        for(int i=1; i<=N; i++){
            q[i] = i;
        }
        int first_index = 1;
        int last_index = N;

        while(N-- > 1){
            first_index++;
            q[last_index + 1] = q[first_index];
            last_index++;
            first_index++;
        }
        System.out.println(q[last_index]);
    }

}
