package WEEK7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Map;
import java.util.StringTokenizer;

public class b_2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());


        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int buget = Integer.parseInt(br.readLine()); // 총 예산
        int start = 0; // 최소 예산
        int end = arr[N-1]; // 최대 예산

        while(start <= end){
            int mid = (start + end)/2; // 상한액
            int b = 0; // 상한액으로 얻을 수 있는 예산
            for(int i=0; i<N; i++){
                if(arr[i] > mid)
                    b += mid;
                else
                    b += arr[i];
            }

            if(b <= buget){
                start = mid+1;
            }else{
                end = mid-1;
            }
        }
        System.out.println(end);
    }
}
