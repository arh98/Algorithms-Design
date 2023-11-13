import java.util.Scanner;

public class Eleven {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) {
            heights[i] = scanner.nextInt();
        }
        System.out.println(maxWater(heights, n));
    }

    public static int maxWater(int[] heightsArr, int n) {
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];

        leftMax[0] = heightsArr[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], heightsArr[i]);
        }

        rightMax[n - 1] = heightsArr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], heightsArr[i]);
        }

        int waters = 0;
        for (int i = 0; i < n; i++) {
            int minHeight = Math.min(leftMax[i], rightMax[i]);
            if (minHeight > heightsArr[i]) {
                waters += minHeight - heightsArr[i];
            }
        }

        return waters;
    }
}
