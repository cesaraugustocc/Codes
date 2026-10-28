// Verificação de matriz simétrica
// Leia uma matriz quadrada 4×4 e verifique se ela é simétrica em relação à diagonal principal. Uma matriz é simétrica quando o elemento da linha i, coluna j é igual ao elemento da linha j, coluna i. Exiba se a matriz é simétrica ou não.


import java.util.Scanner;

public class ex15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrizNumeros = new int[4][4];
        Boolean checagemSimetrica = true;

        for (int i = 0; i < matrizNumeros.length; i++) {
            System.out.println("\nMatriz " + (i));
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matrizNumeros[i][j] = scanner.nextInt();
            }
        }

        for (int i = 0; i < matrizNumeros.length; i++) {
            for (int j = 0; j < matrizNumeros[i].length; j++) {
                if (matrizNumeros[i][j] != matrizNumeros[j][i]) {
                    checagemSimetrica = false;
                }
            }
        }

        if (checagemSimetrica == true) {
            System.out.println("\nA matriz é simétrica");
        } else {
            System.out.println("\nA matriz nao é simétrica");
        }

        scanner.close();
    }
}