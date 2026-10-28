// Leia um número inteiro N e crie uma matriz quadrada N×N. Preencha a diagonal principal com 1 e todas as outras posições com 0. Exiba a matriz.

import java.util.Scanner;

public class ex09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o N da matriz NxN: ");
        int n = scanner.nextInt();

        int[][] matriz = new int[n][n];

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if (i == j) {
                    matriz[i][j] = 1;
                } else {
                    matriz[i][j] = 0;
                }
            }
        }

        for (int[] i : matriz) {
            System.out.println();
            for (int j : i) {
                System.out.print(j);
            }
        }

        scanner.close();
    }
}