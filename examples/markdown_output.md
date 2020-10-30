## Testing all submissions for Homework 01

**4 submissions have been tested.**




---




#### <span style='color: rgb(0, 200, 0)'>Max Mustermann01 -> Successful until execution:</span>

**Output Stream:**

```bash
Testing calc_h...
Testing calc_n...
Failed for H = 0.000000:
Your function returns 1
Correct result would be 0

Failed for H = 1.000000:
Your function returns 2
Correct result would be 1

Passed 18 of 20 cases.

Submission passed! Congratulations!
```


**Input File `partial_sum.c`:**

```c

/*****************************************************************
* Name: Max Mustermann 01
* Course: MSE Informatik I
* Semester: WS19/20
* Homework 1:N-th partial sum
* File: partial_sum.c
* File type: Template file
*****************************************************************/

#include <stdio.h>
#include <stdlib.h>


/**
* calc_h
*
* This function calculates the n-th partial sum of the harmonic series
*
*
* @param n number of partials (assume n>=0)
*
* @return n-th partial sum of harmonic series H(n)
*/
double calc_h(int n){
    //Your code starts here

    double H = 0.0;
    for (double i = 1.0; i <= n; i ++){

        H = H + 1/i;

    }

return H;

    //End of your code
}



/**
* calc_n
*
* This function calculates the smallest n, for which the n-th
* partial sum of the harmonic series is larger than or equal to the input h
*
*
* @param h input h (assume h >=0)
*
* @return smallest n, with H(n) >= h
*/
int calc_n(double h){
    //Your code starts here
    int i = 0;

    while(h >= 0){
        i++;
        h = h - 1.0 / i;
    }
    return i;
    //End of your code
}


```




---




#### <span style='color: rgb(0, 200, 0)'>Max Mustermann02 -> Successful until execution:</span>

**Output Stream:**

```bash
Testing calc_h...
Testing calc_n...
Passed 20 of 20 cases.

Submission passed with merit! Congratulations!
```


**Input File `partial_sum.c`:**

```c

/*****************************************************************
* Name: Max Mustermann 02
* Course: MSE Informatik I
* Semester: WS19/20
* Homework 1:N-th partial sum
* File: partial_sum.c
* File type: Template file
*****************************************************************/

#include <stdio.h>
#include <stdlib.h>


/**
* calc_h
*
* This function calculates the n-th partial sum of the harmonic series
*
*
* @param n number of partials
*
* @return n-th partial sum of harmonic series H(n)
*/

double sum;
int n;
double s;

double calc_h(int n){
    //Your code starts here
    sum = 0;
    for (int i = 1; i <= n; i++) {
        sum = sum + 1.0/i;
    }
    return sum;
    //End of your code
}



/**
* calc_n
*
* This function calculates the smallest n, for which the n-th
* partial sum of the harmonic series is larger than or equal to the input h
*
*
* @param h input h
*
* @return smallest n, with H(n) >= h
*/

int calc_n(double h) {
    //Your code starts here
    s = 0;
    n = 0;
    while (1) {
        if (s>=h) {
            break;
        }
        n++;
        s = s + 1.0/n;
        }
    return n;


    //End of your code
}


```




---




#### <span style='color: rgb(255, 0, 0)'>Max Mustermann03 -> Failed:</span>


```bash
Did not compile: In file included from HW1/submission/Submission_Max_Mustermann03/main_partial_correction.c:11:
HW1/submission/Submission_Max_Mustermann03/partial_sum.c:29:16: error: expected expression
    while (i < = n);
               ^
1 error generated.

```


**Input File `partial_sum.c`:**

```c

/*****************************************************************
* Name: Max Mustermann 03
* Course: MSE Informatik I
* Semester: WS19/20
* Homework 1:N-th partial sum
* File: partial_sum.c
* File type: Template file
*****************************************************************/

#include <stdio.h>
#include <stdlib.h>


/**
* calc_h
*
* This function calculates the n-th partial sum of the harmonic series
*
*
* @param n number of partials (assume n>=0)
*
* @return n-th partial sum of harmonic series H(n)
*/
double calc_h(int n){
    //Your code starts here
    double H = 0;
    double i = 1;
    while (i < = n);
    {
        H+=1/i;
        i++;
    }
    return H;
    //End of your code
}



/**
* calc_n
*
* This function calculates the smallest n, for which the n-th
* partial sum of the harmonic series is larger than or equal to the input h
*
*
* @param h input h (assume h >=0)
*
* @return smallest n, with H(n) >= h
*/
int calc_n(double h){
    //Your code starts here
    double f = 0.0;
    if (h == 0) {

        return f = 0;
    }

    while (h > 0){

        h=h -1 / f;
        f ++;

    }
    return f -= 1;
    //End of your code
}


```




---




#### <span style='color: rgb(255, 0, 0)'>Max Mustermann04 -> Failed:</span>


```bash
Wrong files in zip-file: Desired: ['HW1_Mustermann04_Max.zip', 'partial_sum.c'], Actual: ['New folder', '__MACOSX', 'HW1_Mustermann04_Max.zip']
```





---




