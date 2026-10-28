// Leia uma matriz quadrada de ordem 4 e calcule a soma dos elementos da diagonal principal e da diagonal secundária. Exiba os dois resultados separadamente.

import java.util.Scanner;

public class ex02 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int[][] numero = new int[4][4];
        int somaDiagon = 0;

        for (int i = 0; i < numero.length; i++) {
            System.out.println("\nArray " + i);

            for (int j = 0; j < numero[i].length; j++) {
                System.out.print("Digite o valor do array " + "[" + i + "]" + "[" + j + "]" + ": ");
                numero[i][j] = scanner.nextInt();

                if (i == j) { // poderia unificar as 2 por um or, mas dessa forma posso separar as diagonais
                    somaDiagon += numero[i][j];
                }

                if (i + j == 3) {
                    somaDiagon += numero[i][j];
                }
            }

        }

        System.out.println("A soma das diagonais é: " + somaDiagon);
        scanner.close();
    }
}