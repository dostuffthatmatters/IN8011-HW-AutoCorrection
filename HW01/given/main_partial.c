
/*****************************************************************
* Name: Philipp Kaeß
* Course: MSE Informatik I
* Semester: WS20/21
* Homework 1:N-th partial sum
* File: main_partial.c
* File type: Testing
*****************************************************************/


#include "partial_sum.c"
#include <math.h>

int passed = 0;
int failed = 0;

void testing_calc_h(){
    int n[5]={0, 1, 1000, 2000, 272400599};
    double real_H[5]={0.00000000000000000000, 1.00000000000000000000, 7.48547086055034330000, 8.17836810361028380000, 19.99999999794066200000};
    double your_H[5]={0};
    for(int i=0; i<5; i++){
        your_H[i]=calc_h(n[i]);
    }

    for(int i=0; i<5; i++){
        if(fabs(your_H[i] - real_H[i])>0.00001){
            failed++;
            printf("Failed for n = %d:\nYour function returns %.18lf\nCorrect result would be %.18lf\n\n",n[i],your_H[i],real_H[i]);
        }
        else{
            passed++;
        }
    }
}

void testing_calc_n(){
    double H[5]={0.0, 4.2, 5.0, 10.5, 20.0};
    int real_n[5]={0, 37, 83, 20390, 272400600};
    int your_n[5]={0};
    for(int i=0; i<5; i++){
        your_n[i]=calc_n(H[i]);
    }

    for(int i=0; i<5; i++){
        if(your_n[i] != real_n[i]){
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


}
