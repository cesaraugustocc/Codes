// Leia as notas de 5 alunos em 4 disciplinas, armazenando-as em uma matriz 5×4. Calcule e mostre a média de cada aluno. Informe também quantos alunos obtiveram média igual ou superior a 7.

import java.util.Scanner;

public class ex10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int [][] matrizAlunos = new int[5][4];
        int [] mediaAlunos = new int[5];
        int somaNotas = 0;
        int quantidAlunosMediaSup7 = 0;
        int contador = 1;

        for (int i = 0; i < matrizAlunos.length; i++){
            System.out.println("\nAluno " + (i + 1));
            for (int j = 0; j < matrizAlunos[i].length; j++){
                System.out.print("Digite a nota na prova " + (j + 1) + ": ");
                matrizAlunos[i][j] = scanner.nextInt();
                somaNotas += matrizAlunos[i][j];
                mediaAlunos[i] = somaNotas/4;

                if (mediaAlunos[i] >= 7){
                    quantidAlunosMediaSup7++;
                }
            }
            somaNotas = 0;
        }

        System.out.println();
        for (int i : mediaAlunos){
            System.out.println("Média aluno "+contador+": "+i);
            contador++;
        }

        System.out.println("\nQuantidade de alunos com média >= 7: "+quantidAlunosMediaSup7);

        scanner.close();
    }
}