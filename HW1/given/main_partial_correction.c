
/*****************************************************************
* Name: ---
* Course: MSE Informatik I
* Semester: WS19/20
* Homework 1:N-th partial sum
* File: main_partial_correction.c
* File type: Correction
*****************************************************************/

#include "partial_sum.c"
#include <math.h>
#include <stdio.h>

int passed = 0;
int failed = 0;

double fabs_val (double input) {
    if (input < 0) {
        return input * (-1);
    } else {
        return input;
    }
}

void testing_calc_h(){
    int n[10]={0, 1, 2, 10, 100, 1000, 2000, 12345,123456, 272400599};
    double real_H[10]={0.00000000000000000000, 1.00000000000000000000, 1.50000000000000000000, 2.92896825396825380000, 5.18737751763962060000, 7.48547086055034330000, 8.17836810361028380000, 9.99826256836159110000, 12.30085981118720900000, 19.99999999794066200000};
    double your_H[10]={0};
    for(int i=0; i<10; i++){
        your_H[i]=calc_h(n[i]);
    }

    for(int i=0; i<10; i++){
        if(fabs_val(your_H[i] - real_H[i])> 0.00001){
            failed++;
            printf("Failed for n = %d:\nYour function returns %.18lf\nCorrect result would be %.18lf\n\n",n[i],your_H[i],real_H[i]);
        }
        else{
            passed++;
        }
    }
}

void testing_calc_n(){
    double H[10]={0.0, 0.5, 1.0, 2.0, 4.2, 5.0, 10.5, 15.0, 17.3,20.0};
    int real_n[10]={0, 1, 1, 4, 37, 83, 20390, 1835421, 18306822, 272400600};
    int your_n[10]={0};
    for(int i=0; i<10; i++){
        your_n[i]=calc_n(H[i]);
    }

    for(int i=0; i<10; i++){
        if(fabs_val(your_n[i] - real_n[i])> 0.00001){
            failed++;
            printf("Failed for H = %f:\nYour function returns %d\nCorrect result would be %d\n\n",H[i],your_n[i],real_n[i]);
        }
        else{
            passed++;
        }
    }
}

int main() {

    printf("Testing calc_h...\n");
    testing_calc_h();

    printf("Testing calc_n...\n");
    testing_calc_n();

    printf("Passed %d of %d cases.\n\n",passed, passed+failed);

    if(passed==20){
        printf("Submission passed with merit! Congratulations!");
    }
    else if(passed>=16){
        printf("Submission passed! Congratulations!");
    }
    else{
        printf("Submission failed.");
    }
}
