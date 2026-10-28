// Leia uma matriz 3×4 e gere sua matriz transposta, que deverá ter 4 linhas e 3 colunas. Exiba as duas matrizes.

import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] matriz = new int[3][4];
        int[][] matrizTransposta = new int[4][3];

        for (int i = 0; i < matriz.length; i++) {

            System.out.println("\nMatriz " + i);

            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matriz[i][j] = scanner.nextInt();
                matrizTransposta[j][i] = matriz[i][j];
            }
        }

        System.out.println("\nMatriz Original 3x4");

        for (int[] i : matriz) {
            System.out.println();
            for (int j : i) {
                System.out.print(j + " ");
            }
        }

        System.out.println("\n\nMatriz Transposta 4x3");

        for (int[] i : matrizTransposta) {
            System.out.println();
            for (int j : i) {
                System.out.print(j + " ");
            }
        }
        scanner.close();
    }
}