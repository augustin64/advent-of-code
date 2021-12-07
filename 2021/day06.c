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

list* read_sample() {
    FILE *fp;
    char ch;
    list* l = NULL;
    fp = fopen( "inputs/day06.txt", "r");
    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    };

    while((ch = fgetc(fp)) != EOF) {
        if (ch != ',' && ch != '\n' ) {
            l = add(l, ch - '0');
        };
    };
    fclose(fp);
    return l;
};

int part1(list* sample, int days) {
    list* start = sample;
    for (int i=-1; i < days+1; i++) {
        while(sample!=NULL) {
            if (sample->elem==i-1) {
                sample->elem = i+6;
                start = add(start, i+8);
            };
            sample = sample->next;
        };
        sample = start;
        printf("After %d days: %d\n", i, size(sample));
    };
    return size(start);
};

/*int part2(list* sample, int days) {
    int tab[8];
    int tmp;
    int somme = 0;

    for (int i=0; i < 8; i++) {
       tab[i] = 0; 
    };
    while (sample!=NULL) {
        tab[sample->elem]++;
        sample = sample->next;
    };
    for (int i=0; i < days+1; i++) {
        tmp = tab[i%8];
        tab[(i+6)%8] += tmp;
        printf("%d\n", tmp);
    };

    for (int i=0; i < 8; i++) {
        somme += tab[i];
    }
    return somme;
};*/

int main() {
    list* l1 = read_sample();
    //list* l2 = read_sample();
    printf("Partie 1: %d\n", part1(l1, 80));
    //printf("Partie 2: %d\n", part2(l2, 256));
    // La partie II menant à des nombres trop grands,
    // la gestion d'overflow devenant un problème, elle
    // a été réalisée en Python
    return 0;
};
