// Leia uma matriz 5×5 de números inteiros. Ao final, informe quantos elementos são pares e quantos são ímpares.

import java.util.Scanner;

public class ex07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matriz = new int[5][5];
        int par = 0;
        int impar = 0;

        for (int i = 0; i < matriz.length; i++) {
            System.out.println("\nMatriz " + i);

            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Digite o valor de " + "[" + i + "]" + "[" + j + "]: ");
                matriz[i][j] = scanner.nextInt();

                if (matriz[i][j] % 2 == 0){
                    par++;
                }else{
                    impar++;
                }
            }
        }

        System.out.println("\nTotal de números pares: "+par);
        System.out.println("Total de números ímpares: "+impar);

        scanner.close();
    }

}