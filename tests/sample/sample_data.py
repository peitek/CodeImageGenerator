content_contains_substring = """public static void main() {
    String word = "Hamburg";
    String substring = "burg";
    System.out.print(containsSubstring(word, substring));
}

public static boolean containsSubstring(String word, String substring) {
    boolean containsSubstring = false;

    for (int i = 0; i < word.length(); i++) {
        for (int j = 0; j < substring.length(); j++) {
            if (i + j >= word.length())
                break;
            if (word.charAt(i + j) != substring.charAt(j)) {
                break;
            } else {
                if (j == substring.length() - 1) {
                    containsSubstring = true;
                    break;
                }
            }
        }
    }

    return containsSubstring;
}"""

content_average_substring = """public static void main() {
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
}"""
