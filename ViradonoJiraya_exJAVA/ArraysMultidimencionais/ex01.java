// Crie uma matriz de 4 linhas e 3 colunas para armazenar as notas de 4 alunos em 3 provas. Leia as notas e mostre a matriz completa na tela.

import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int [][] notas = new int [4][3];
        int contador = 1;
        int contador2 = 1;

        for (int i = 0; i < notas.length; i++){
            System.out.println("\nAluno "+(i+1)+"\n");

            for (int j = 0; j < notas[i].length; j++){
                System.out.print("Digite a nota da prova "+(j+1)+": ");
                notas[i][j] = scanner.nextInt();
            }
        }

        System.out.println("\n-=- NOTAS -=-");

        for (int[] i : notas ){
            System.out.println("\nAluno "+contador+"\n");
            contador++;

            for (int j : i){
                System.out.println("Prova "+contador2+": "+j);
                contador2++;
            }
            contador2 = 1;
        }
        
        scanner.close();
    }
}