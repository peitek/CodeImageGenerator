public static void main() {
    int[] input = {2, 4, 1, 9};
    System.out.print(arrayAverage(input));
}

public static float arrayAverage(int[] numbers) {
    int count = 0;
    int sum = 0;

    while (count < numbers.length) {
        sum = sum + numbers[count];
        count = count + 1;
    }

    float average = sum / (float) count;
    return average;
}