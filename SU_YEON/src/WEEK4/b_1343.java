package WEEK4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_1343 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));

        String board = br.readLine();

        board = board.replace("XXXX","AAAA");
        board = board.replace("XX", "BB");

        if(board.contains("X")){
            System.out.println("-1");
        }else
            System.out.println(board);
    }
}
