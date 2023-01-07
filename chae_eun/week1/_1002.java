package boj.sliver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1002 {
// 원들의 접점을 구하는 것
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		try {
			T = Integer.parseInt(br.readLine());
			for(int i = 0; i<T; i++) {
				String answer = br.readLine();
				StringTokenizer st = new StringTokenizer(answer, " ");
				
				int x1 = Integer.parseInt(st.nextToken());
				int y1 = Integer.parseInt(st.nextToken());
				int r1 = Integer.parseInt(st.nextToken());
				int x2 = Integer.parseInt(st.nextToken());
				int y2 = Integer.parseInt(st.nextToken());
				int r2 = Integer.parseInt(st.nextToken());
				
				int r = (int)(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2)); // 두 점 사이의 거리의 제곱 구하기

				// 접점 무한 대
					// x1 = x2, y1 = y2, r1 = r2일 때
				if(x1 == x2 && y1 == y2 && r1 == r2) {
					System.out.println(-1);
				}
				// 접점 1개
					// 외접: r1 + r2 = r인 경우 접점 1개
				else if(r == Math.pow(r1+r2, 2)) {
					System.out.println(1);
				}
					// 내접
				else if(r == Math.pow(r2-r1, 2)) {
					System.out.println(1);
				}
				// 접점이 없을 때
					// 내부: 한 원이 다른 원보다 월등히 작은 경우
				else if(r <Math.pow(r2-r1, 2)) {
					System.out.println(0);
				}
					// 외부: 두 원이 서로 접점이 없는 경우
				else if(r> Math.pow(r1+r2, 2)) {
					System.out.println(0);
				}

				else { // 접점이 두개인 경우
					System.out.println(2);
				}
			}
		} catch (NumberFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}
