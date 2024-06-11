// 설탕 배달

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int result = -1;

        in.close();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (3 * i + 5 * j == N) {
                    result = i + j;
                    System.out.println(result);
                    return ;
                }
            }
        }
        System.out.println(result);
    } 
}