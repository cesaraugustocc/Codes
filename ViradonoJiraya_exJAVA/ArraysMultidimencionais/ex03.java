// Crie uma matriz 3×3 preenchida com o caractere -. Permita que o usuário informe uma linha e uma coluna para colocar o caractere X. Ao final, mostre o tabuleiro atualizado.

import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[][] matriz = { { "-", "-", "-" }, { "-", "-", "-" }, { "-", "-", "-" } };

        System.out.println("=-= Matriz principal =-=");

        for (String[] i : matriz) {
            System.out.println();
            for (String j : i) {
                System.out.print(j);
            }
        }

        System.out.println("\n");

        System.out.print("Digite a linha que você deseja adicionar um 'x', 0-2: ");
        int linha = scanner.nextInt();

        System.out.print("Digite a coluna que você deseja adicionar um 'x', 0-2: ");
        int coluna = scanner.nextInt();

        matriz[linha][coluna] = "X";

        System.out.println("\n-=- Matriz Modificada -=-");

        for (String[] i : matriz) {
            System.out.println();
            for (String j : i) {
                System.out.print(j);
            }
        }

        scanner.close();
    }
}