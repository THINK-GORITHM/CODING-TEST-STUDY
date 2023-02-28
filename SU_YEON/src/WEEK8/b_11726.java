package WEEK8;

import java.io.*;

public class b_11726 {

    public static final int mod = 10007;

    public static void main(String[] arsg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 2;
        for(int i=3; i<=n; i++){
            dp[i] = (dp[i-1] + dp[i-2]) % mod;
        }
        System.out.println(dp[n]);
    }
}
