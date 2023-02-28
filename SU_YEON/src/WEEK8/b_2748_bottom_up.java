package WEEK8;

import java.io.*;

public class b_2748_bottom_up {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int first = 0;
        int second = 1;
        int result = 0;

        for(int i=0; i<n+1; i++){
            result = first+second;
            first = second;
            second = result;
        }
        System.out.println(result);
    }
}
