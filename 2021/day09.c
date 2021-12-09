#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

typedef struct list list;

struct list {
    list* next;
    int elem;
};

list* add(list* l, int e) {
    list* l_new = (list*)malloc(sizeof(int)+sizeof(list*));
    l_new->next = l;
    l_new->elem = e;
    return l_new;
};

bool has(list *l, int e) {
    while (l != NULL) {
        if (l->elem==e) {
            return true;
        };
        l=l->next;
    };
    return false;
};

int size(list* l) {
    int n = 0;
    while (l!= NULL) {
        n++;
        l = l->next;
    };
    return n;
};

void print_list(list* l) {
    while (l != NULL) {
        printf("%d->", l->elem);
        l = l->next;
    };
    printf("NULL\n");
};

int value_of(list* l) {
    int somme = 0;
    while (l!=NULL) {
        somme += 1 + l->elem;
        l = l->next;
    };
    return somme;
};

int* read_sample() {
    FILE *fp;
    char ch;
    int length = 0;
    fp = fopen( "inputs/day09.txt", "r");
    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    };
    while(fgetc(fp) != EOF) {
        length++;
    };

    int* tab = (int*)malloc(sizeof(int)*length);

    fclose(fp);
    
    fp= fopen("inputs/day09.txt", "r");
    if (fp==NULL){
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    };
    int i=0;
    while((ch=fgetc(fp))!=EOF) {
        if (ch != '\n') {
            tab[i] = ch - '0';
            i++;
        };
    };
    return tab;
};

int part1(int* sample, int n, int p) {
    list* l = NULL;
    bool cur;
    for (int i=0; i < n; i++) {
        for (int j=0; j < p; j++) {
            cur = true;
            cur = cur && (j == 0||sample[i*p+j]<sample[i*p+j-1]);
            cur = cur && (j==p-1||sample[i*p+j]<sample[i*p+j+1]);
            cur = cur && (i == 0||sample[i*p+j]<sample[i*p+j-p]);
            cur = cur && (i==n-1||sample[i*p+j]<sample[i*p+j+p]);
            if (cur) {
                l = add(l, sample[i*p+j]);
            };
        };
    };
    return value_of(l);
};


int main() {
    int n = 100;
    int p = 100;
    int* tab = read_sample();
    printf("Partie 1: %d\n", part1(tab, n, p));
    return 0;
}
