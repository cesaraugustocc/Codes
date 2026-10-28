// Molde pronto de um Array Multidimencional que o lê e o imprime

import java.util.Scanner;

public class matrizLeitura {
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

        System.out.println("\nForeach\n");
        for (int[] i : matrizNumeros){
            System.out.println();
            for (int j : i){
                System.out.print(j);
            }
        }
        
        scanner.close();
    }
}