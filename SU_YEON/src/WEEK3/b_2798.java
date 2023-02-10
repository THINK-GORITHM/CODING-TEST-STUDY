package WEEK3;

import java.io.*;
import java.util.StringTokenizer;

public class b_2798 {

    static int search(int[] arr, int N, int M){

        int result = 0;

        for(int i=0; i<N-2; i++){
            for(int j=i+1; j<N-1; j++){
                for(int k=j+1; k<N; k++){
                    int temp = arr[i]+arr[j]+arr[k];

                    if(temp == M){
                        return temp;
                    }

                    if(result<temp && temp < M){
                        result = temp;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] cardArr = new int[N];

        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<cardArr.length; i++){
            cardArr[i] = Integer.parseInt(st.nextToken());
        }

        int result = search(cardArr, N, M);
        System.out.println(result);
    }
}
