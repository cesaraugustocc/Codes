// Existem 3 candidatos e 5 zonas eleitorais. Crie uma matriz 3×5 que armazene os votos de cada candidato em cada zona. 
// Calcule o total de votos por candidato e informe quem venceu. Considere que não haverá empate.

import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrizVotos = new int[3][5];
        int somaVotos = 0;
        int maiorSomaVotos = 0;
        int candidatoVencedor = 0;

        for (int i = 0; i < matrizVotos.length; i++) {
            System.out.println("\nCaditadato " + (i + 1));
            for (int j = 0; j < matrizVotos[i].length; j++) {
                System.out.print("Digite o número de votos na zona " + (j + 1) + ": ");
                matrizVotos[i][j] = scanner.nextInt();
                somaVotos += matrizVotos[i][j];

                if (somaVotos > maiorSomaVotos) {
                    maiorSomaVotos = somaVotos;
                    candidatoVencedor = i + 1;
                }
            }

            somaVotos = 0;
        }

        System.out.println("\nCandidato " + candidatoVencedor + ", venceu!\nTotal de " + maiorSomaVotos + " votos.");

        scanner.close();
    }
}