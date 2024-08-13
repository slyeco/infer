// test_classifier.c
#include <stdio.h>
#include "classifier.h"  // Make sure this points to the correct path

int main() {
    double input[10] = {361800,73594600,71839900,70506700,4187000,4183800,4171000,381900,404100,429200};
    double output[2];

    // Call the classifier's score function
    score(input, output);

    // Print the output
    printf("Inference value (output[0]): %f\n", output[0]);
    printf("Inference value (output[1]): %f\n", output[1]);

    return 0;
}