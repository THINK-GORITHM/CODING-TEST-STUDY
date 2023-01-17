package WEEK3;

import java.io.*;
import java.util.Arrays;

public class b_2309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dwarfArr = new int[9];

        int sum = 0;
        int spy1 = 0, spy2 = 0;

        for(int i=0; i<dwarfArr.length; i++){
            dwarfArr[i] = Integer.parseInt(br.readLine());
            sum += dwarfArr[i];
        }
        Arrays.sort(dwarfArr);

        for(int i=0; i<dwarfArr.length-1; i++){
            for(int j=i+1; j<dwarfArr.length; j++){
                if(sum - dwarfArr[i] - dwarfArr[j] == 100){
                    spy1 = i;
                    spy2 = j;
                }
            }
        }
        for(int i=0; i<dwarfArr.length; i++){
            if(!(i == spy1 || i == spy2))
                System.out.println(dwarfArr[i]);
        }
    }
}
