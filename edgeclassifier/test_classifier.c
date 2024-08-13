// test_classifier.c
#include <stdio.h>
#include <stdlib.h>  // For atof()
#include "classifier.h"

int main(int argc, char *argv[]) {
    double input[10] = {361800, 73594600, 71839900, 70506700, 4187000, 4183800, 4171000, 381900, 404100, 429200};
    double output[2];

    // Print the command-line arguments for debugging
    printf("argc: %d\n", argc);
    for (int i = 0; i < argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }

    // If command-line arguments are provided, overwrite the default values
    if (argc > 1) {
        for (int i = 1; i < argc && i <= 10; i++) {
            input[i - 1] = atof(argv[i]);  // Convert argument to double and store in input array
        }
    }

    // Print the input values before running the inference
    printf("Input values:\n");
    for (int i = 0; i < 10; i++) {
        printf("input[%d]: %f\n", i, input[i]);
    }

    // Call the classifier's score function
    score(input, output);

    // Print the output
    printf("Inference value Air (output[0]): %f\n", output[0]);
    printf("Inference value Smoke (output[1]): %f\n", output[1]);

    return 0;
}
