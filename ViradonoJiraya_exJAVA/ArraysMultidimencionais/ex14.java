// Leia uma matriz 4×4 de números inteiros. Ordene os elementos de cada linha em ordem crescente, sem alterar a posição das linhas. Exiba a matriz original e a matriz ordenada.

import java.util.Scanner;
import java.util.Arrays;

public class ex14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrizNumeros = new int[4][4];

        for (int i = 0; i < matrizNumeros.length; i++) {
            System.out.println("\nMatriz " + (i));
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matrizNumeros[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\nMatriz Original\n");
        for (int[] i : matrizNumeros) {
            System.out.println();
            for (int j : i) {
                System.out.print(j+" ");
            }
        }

        System.out.println("\n\nMatriz Organizada");
        for (int i = 0; i < matrizNumeros.length; i++) {
            Arrays.sort(matrizNumeros[i]);
            System.out.println();
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                System.out.print(matrizNumeros[i][j]+" ");
            }
        }
        scanner.close();
    }
}