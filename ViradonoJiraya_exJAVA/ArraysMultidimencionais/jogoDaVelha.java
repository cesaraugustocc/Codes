/*Tive a ideia de criar um jogo da velha **INTERMINADO**
O código apresenta apenas a estrutura mas não tem regra de jogo nem jogadores
Talvez algum dia termine */

import java.util.Scanner;

public class jogoDaVelha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[][] matriz = { { "-", "-", "-" }, { "-", "-", "-" }, { "-", "-", "-" } };

        System.out.println("--- Matriz principal ---");

        for (String[] i : matriz) {
            System.out.println();
            for (String j : i) {
                System.out.print(j);
            }
        }

        for (int i = 0; i < matriz.length; i++) {
            System.out.print("\n\nDigite a linha que você deseja adicionar um 'X', 0-2: ");
            int linha = scanner.nextInt();

            System.out.print("Digite a coluna que você deseja adicionar um 'X', 0-2: ");
            int coluna = scanner.nextInt();

            matriz[linha][coluna] = "X";

            System.out.println("\nResultado Atual");

            for (String[] k : matriz) {
                System.out.println();
                for (String j : k) {
                    System.out.print(j);
                }
            }

            System.out.print("\n\nDigite a linha que você deseja adicionar um 'O', 0-2: ");
            linha = scanner.nextInt();

            System.out.print("Digite a coluna que você deseja adicionar um 'O', 0-2: ");
            coluna = scanner.nextInt();

            matriz[linha][coluna] = "O";

            for (String[] k : matriz) {
                System.out.println();
                for (String j : k) {
                    System.out.print(j);
                }
            }
        }
        scanner.close();
    }
}
