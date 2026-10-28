// Leia uma matriz 4×4 e depois solicite um número ao usuário. Informe todas as posições em que esse número aparece, usando índices de linha e coluna começando em zero. Se não aparecer, exiba uma mensagem apropriada.

import java.util.Scanner;

public class ex13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrizNumeros = new int[4][4];
        Boolean checagemExisteNumeroMatriz = false;

        for (int i = 0; i < matrizNumeros.length; i++) {
            System.out.println("\nMatriz " + (i));
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matrizNumeros[i][j] = scanner.nextInt();
            }
        }

        System.out.print("\nDigite um número para se localizar na matriz: ");
        int numeroLocalizar = scanner.nextInt();

        System.out.println();
        for (int i = 0; i < matrizNumeros.length; i++) {
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                if (matrizNumeros[i][j] == numeroLocalizar) {
                    System.out.println(
                            "Número " + numeroLocalizar + " localizado na posiçao " + "[" + i + "]" + "[" + j + "]");
                    checagemExisteNumeroMatriz = true;
                }
            }
        }

        if (checagemExisteNumeroMatriz == false) {
            System.out.println("\nNao foi encontrado o número " + numeroLocalizar + " na matriz");
        }

        scanner.close();
    }
}