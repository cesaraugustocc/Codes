// Leia uma matriz 5×5 de números inteiros. Para cada linha, encontre o maior número de elementos consecutivos iguais. Por exemplo, na linha 2 2 2 4 4, o resultado é 3. Mostre o resultado de cada linha.

import java.util.Scanner;

public class ex12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrizNumeros = new int[5][5];
        int contadorNumeroSequencia = 1;
        int contadorNumeroSequenciaAtual = 1;

        for (int i = 0; i < matrizNumeros.length; i++) {
            System.out.println("\nMatriz " + (i));
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matrizNumeros[i][j] = scanner.nextInt();

                if (j > 0) {
                    if (matrizNumeros[i][j] == matrizNumeros[i][j - 1]) {
                        contadorNumeroSequenciaAtual++;
                    } else {
                        contadorNumeroSequenciaAtual = 1;
                    }

                    if (contadorNumeroSequenciaAtual > contadorNumeroSequencia) {
                        contadorNumeroSequencia = contadorNumeroSequenciaAtual;
                    }
                }
            }

            System.out.println("\nQuantidade de vezes que o maior número apareceu em sequência: " + contadorNumeroSequencia);

            contadorNumeroSequencia = 1;
            contadorNumeroSequenciaAtual = 1;
        }
        scanner.close();
    }
}