// Leia duas matrizes quadradas 3×3. Crie uma terceira matriz que armazene o resultado da multiplicação entre elas. Exiba as duas matrizes originais e a matriz resultante.

import java.util.Scanner;

public class ex11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matriz1 = new int[3][3];
        int[][] matriz2 = new int[3][3];
        int[][] matrizSoma = new int[3][3];
        
        System.out.println("\n-------------\n\nMatriz 1\n\n-------------");

        for (int i = 0; i < matriz1.length; i++) {
            System.out.println("\nMatriz " + i);

            for (int j = 0; j < matriz1[i].length; j++) {
                System.out.print("Digite o valor do array " + "[" + i + "]" + "[" + j + "]" + ": ");
                matriz1[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\n-------------\n\nMatriz 2\n\n-------------");

        for (int i = 0; i < matriz2.length; i++) {
            System.out.println("\nMatriz " + i);

            for (int j = 0; j < matriz2[i].length; j++) {
                System.out.print("Digite o valor do array " + "[" + i + "]" + "[" + j + "]" + ": ");
                matriz2[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\n-------------\n\nSoma Matrizes\n\n-------------");

        for (int i = 0; i < matrizSoma.length; i++) {
            System.out.println();

            for (int j = 0; j < matrizSoma[i].length; j++) {
                matrizSoma[i][j] = matriz1[i][j] + matriz2[i][j];
                System.out.print(matrizSoma[i][j]);
            }
        }

        scanner.close();
    }
}