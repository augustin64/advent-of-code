#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

typedef struct list list;

struct list {
    int elem;
    list* next;
};

list* add(list* l, int e) {
    list* l1 = (list*)malloc(sizeof(list));
    l1->elem = e;
    l1->next = l;
    return l1;
};

int value_of(char s) {
    if (s=='<' || s=='>')
        return 25137;
    if (s=='{' || s=='}')
        return 1197;
    if (s=='[' || s==']')
        return 57;
    if (s=='(' || s==')')
        return 3;
    printf("Error, %c occured\n", s);
    return 0;
};

int score(char* line) {
    list* l = NULL;
    list* tmp;
    int i =0;
    while (line[i]!='\0' && line[i]!='\n') {
        if (line[i]=='<'||line[i]=='{'||line[i]=='('||line[i]=='[') {
            l = add(l, value_of(line[i])); 
        } else {
            if (value_of(line[i])==l->elem) {
                tmp = l;
                l = l->next;
                free(tmp);
            } else {
                free(l);
                return value_of(line[i]);
            }
        };
        i++;
    };
    free(l);
    return 0;
}

int part1(char* filename) {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    size_t read;
    int somme = 0;

    fp = fopen(filename, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        somme += score(line);
    }

    fclose(fp);
    return somme;
}

int main() {
    char* filename = "inputs/day10.txt";
    printf("Partie 1: %d\n", part1(filename));
    return 0;
}
