package WEEK2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class b_11286 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> priorityQ = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int A = Math.abs(o1);
                int B = Math.abs(o2);
                if(A > B)
                    return A-B;
                else if (A == B) {
                    if(o1 > 02) return 1;
                    else return -1;
                }
                else
                    return -1;
            }
        });

        while(N-- > 0){
            int num = Integer.parseInt(br.readLine());

            if(num != 0){
                priorityQ.offer(num);
            }
            else{
                if(!priorityQ.isEmpty()){
                    sb.append(priorityQ.poll()).append('\n');
                }
                else
                    sb.append('\n');
            }
        }
        System.out.print(sb);
    }
}
