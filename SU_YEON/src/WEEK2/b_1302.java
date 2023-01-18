package WEEK2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class b_1302 {
    public static void main(String[] args)throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bf.readLine());
        HashMap<String, Integer> book = new HashMap<String, Integer>();
        String str;

        for(int i=0; i<N; i++){
            str = bf.readLine();
            if(book.containsKey(str)){
                book.replace(str, book.get(str)+1);
            }
            else{
                book.put(str, 1);
            }
        }

        int max = 0;
        for(String s : book.keySet()){
            max = Math.max(max, book.get(s));
        }

        ArrayList<String> arr = new ArrayList<String>(book.keySet());
        Collections.sort(arr);
        for(String s : arr){
            if(book.get(s) == max){
                System.out.println(s);
                break;
            }
        }

    }
}
