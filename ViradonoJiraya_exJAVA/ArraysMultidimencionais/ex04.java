// Leia uma matriz 4×4 de números inteiros. Para cada linha, encontre e mostre o maior elemento presente nela.

import java.util.Scanner;

public class ex04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matriz = new int[4][4];
        int maiorNumero = 0;
        int linha = 0;
        int coluna = 0;

        for (int i = 0; i < matriz.length; i++) {
            System.out.println("\nArray " + i);

            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Digite o valor do array " + "[" + i + "]" + "[" + j + "]" + ": ");
                matriz[i][j] = scanner.nextInt();

                if (matriz[i][j] > maiorNumero) {
                    maiorNumero = matriz[i][j];
                    linha = i;
                    coluna = j;
                }
            }
        }

        System.out.println(
                "\nO maior número entre os arrays é: " + "[" + linha + "]" + "[" + coluna + "] = " + maiorNumero);

        scanner.close();
    }
}