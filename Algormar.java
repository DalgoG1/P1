import java.util.Scanner;

public class Algormar {

    public static double minEnergiaAlgormar(int n, int j, int m, int[] pesos) {
        try {
            if (j == 0) {
                return 0;
            }

            // Inicializar DP: dp[i][k][s]
            double[][][] dp = new double[n + 1][j + 1][m + 1];

            // Casos base iniciales
            for (int i = 0; i <= n; i++) {
                for (int s = 0; s <= m; s++) {
                    dp[i][0][s] = 0; // Suma de 0 elementos
                }
            }

            // Llenar el resto con infinito
            for (int i = 0; i <= n; i++) {
                for (int k = 1; k <= j; k++) {
                    for (int s = 0; s <= m; s++) {
                        dp[i][k][s] = Double.POSITIVE_INFINITY;
                    }
                }
            }

            // Casos base y recursión
            for (int i = 1; i <= n; i++) {
                for (int k = 1; k <= j; k++) {
                    for (int s = 0; s <= m; s++) {
                        if (k > i) {
                            dp[i][k][s] = Double.POSITIVE_INFINITY;
                            continue;
                        }

                        if (k == i) {
                            int suma = 0;
                            for (int idx = 0; idx < k; idx++) {
                                suma += pesos[idx];
                            }
                            dp[i][k][s] = suma;
                            continue;
                        }

                        if (k < i && s == 0) {
                            int suma = 0;
                            for (int idx = 0; idx < k; idx++) {
                                suma += pesos[idx];
                            }
                            dp[i][k][s] = suma;
                            continue;
                        }

                        // Opción 1: No incluir el i-ésimo jugador
                        double option1 = dp[i - 1][k][s];

                        // Opción 2: Incluir el i-ésimo jugador con swap
                        double option2 = Double.POSITIVE_INFINITY;
                        int swapsNeeded = i - k;
                        if (s >= swapsNeeded) {
                            option2 = dp[i - 1][k - 1][s - swapsNeeded] + pesos[i - 1];
                        }

                        dp[i][k][s] = Math.min(option1, option2);
                    }
                }
            }

            // Encontrar el mínimo resultado
            double resultado = Double.POSITIVE_INFINITY;
            for (int s = 0; s <= m; s++) {
                resultado = Math.min(resultado, dp[n][j][s]);
            }

            return Double.isInfinite(resultado) ? 0 : resultado;

        } catch (OutOfMemoryError e) {
            return 0;
        } catch (Exception e) {
            return 0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numCasos = scanner.nextInt();

        for (int caseIndex = 0; caseIndex < numCasos; caseIndex++) {
            int n = scanner.nextInt();
            int j = scanner.nextInt();
            int m = scanner.nextInt();
            int[] pesos = new int[n];
            for (int i = 0; i < n; i++) {
                pesos[i] = scanner.nextInt();
            }

            System.out.println((int) minEnergiaAlgormar(n, j, m, pesos));
        }

        scanner.close();
    }
}