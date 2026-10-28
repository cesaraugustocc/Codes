// Uma loja possui 3 produtos e 4 filiais. Crie uma matriz 3×4 para armazenar as quantidades de cada produto em cada filial. Leia os valores e mostre a quantidade total de cada produto somando todas as filiais.

import java.util.Scanner;

public class ex05 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] produtos = new int[3][4];
        int contador = 1;
        int contador2 = 1;

        for (int i = 0; i < produtos.length; i++) {
            System.out.println("\nProduto " + (i + 1));

            for (int j = 0; j < produtos[i].length; j++) {
                System.out.print("Digite a quantidade do produto " + (i + 1) + " na filial " + (j + 1) + ": ");
                produtos[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\n-- Dados --");

        for (int i[] : produtos) {
            System.out.println("\nProduto " + contador);
            contador++;

            for (int j : i) {
                System.out.println("Quantidade filial " + contador2 + ": " + j);
                contador2++;
            }
            contador2 = 1;
        }
        scanner.close();
    }
}