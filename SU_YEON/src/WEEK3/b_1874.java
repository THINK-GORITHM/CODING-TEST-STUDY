package WEEK3;

import java.io.*;
import java.util.*;;

public class b_1874 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        int[] stack = new int[N];

        int idx = 0;
        int start = 0;

        while(N-- > 0){
            int value = Integer.parseInt(br.readLine());

            if(value > start){
                for(int i=start+1; i<=value; i++){
                    stack[idx] = i;
                    idx++;
                    sb.append('+').append('\n');
                }
                start = value;
            }
            else if(stack[idx-1] != value){
                System.out.println("NO");
                return;
            }
            idx--;
            sb.append('-').append('\n');
        }
        System.out.println(sb);

    }
}
