# Questões de Algoritmos

1. **Subarray de soma máxima**  
   Dada uma lista `A` de `n` inteiros (positivos, negativos e zeros), projete um algoritmo que encontre o subarray contínuo que tenha a soma máxima. O algoritmo deve ter complexidade O(n) no pior caso.

2. **Remoção de duplicatas**  
   Dada uma lista `A` de `n` inteiros, projete um algoritmo que remova todos os elementos duplicados, mantendo a ordem original dos elementos. O algoritmo deve ter complexidade O(n) no pior caso.

3. **Matriz diagonal principal**  
   Dada uma matriz quadrada de ordem `n`, projete um algoritmo que retorne a soma dos elementos na diagonal principal da matriz. O algoritmo deve ter complexidade O(n) no pior caso.

4. **Subconjunto com soma específica**  
   Dada uma lista `A` de `n` inteiros e um valor inteiro `S`, projete um algoritmo que verifique se existe um subconjunto de `A` cuja soma seja exatamente `S`. O algoritmo deve ter complexidade O(n · S) no pior caso.

5. **Reordenar uma lista**  
   Dada uma lista `A` de `n` inteiros, projete um algoritmo que reordene os elementos da lista de forma que todos os números negativos apareçam antes dos números positivos, mantendo a ordem relativa entre os negativos e entre os positivos. O algoritmo deve ter complexidade O(n) no pior caso.

6. **Caminho mínimo em matriz**  
   Dada uma matriz de inteiros de tamanho `n × m`, onde cada elemento representa o custo para passar por essa célula, projete um algoritmo que encontre o caminho de custo mínimo do canto superior esquerdo para o canto inferior direito da matriz. O algoritmo deve ter complexidade O(n · m) no pior caso.

7. **Partição de lista**  
   Dada uma lista `A` de `n` inteiros, projete um algoritmo que divida a lista em duas sublistas tal que a soma dos elementos em uma sublista seja igual à soma dos elementos na outra. Se tal partição não for possível, o algoritmo deve retornar um valor que indique isso. O algoritmo deve ter complexidade O(n · sum(A)) no pior caso, onde `sum(A)` é a soma de todos os elementos de `A`.

8. **Balanceamento de parênteses**  
   Dada uma string composta por `n` caracteres contendo apenas parênteses `(` e `)`, projete um algoritmo que determine se a string está balanceada, ou seja, se todo parêntese de abertura tem um correspondente parêntese de fechamento na ordem correta. O algoritmo deve ter complexidade O(n) no pior caso.

9. **Maior subsequência crescente**  
   Dada uma lista `A` de `n` inteiros, projete um algoritmo que retorne o comprimento da maior subsequência crescente contida em `A` (não necessariamente consecutiva). O algoritmo deve ter complexidade O(n log n) no pior caso.

10. **Reorganização da lista com ordem alternada**  
    Dada uma lista `A` de `n` inteiros, projete um algoritmo que reordene os elementos de `A` de forma que os inteiros de índices pares sejam menores que os inteiros de índices ímpares. O algoritmo deve ter complexidade O(n log n) no pior caso.

11. **Maior subsequência comum**  
    Dadas duas listas `A` e `B`, cada uma contendo `n` inteiros, projete um algoritmo que encontre o comprimento da maior subsequência comum entre as duas listas. O algoritmo deve ter complexidade O(n²) no pior caso.

12. **Ordenação em ordem alternada**  
    Dada uma lista `A` contendo `n` inteiros, projete um algoritmo que ordene a lista de forma que os inteiros em índices ímpares sejam em ordem crescente e os inteiros em índices pares sejam em ordem decrescente. O algoritmo deve ter complexidade O(n log n) no pior caso.

13. **Cálculo da mediana de uma lista**  
    Dada uma lista `A` contendo `n` inteiros, projete um algoritmo que retorne a mediana dos elementos da lista. O algoritmo deve ter complexidade O(n) no pior caso.

14. **Matriz espiral**  
    Dada uma matriz de inteiros de tamanho `n × n`, projete um algoritmo que retorne os elementos da matriz em ordem espiral (começando do canto superior esquerdo). O algoritmo deve ter complexidade O(n²) no pior caso.

15. **Verificação de Árvore Binária de Busca (BST)**  
    Dada uma árvore binária contendo `n` nós, onde cada nó armazena um valor inteiro, projete um algoritmo que determine se a árvore é uma árvore binária de busca (BST) válida. O algoritmo deve ter complexidade O(n) no pior caso.

16. **Contagem de inversões**  
    Dada uma lista `A` contendo `n` inteiros, projete um algoritmo que conte o número de inversões na lista. Uma inversão é um par de índices `(i, j)` tal que `i < j` e `A[i] > A[j]`. O algoritmo deve ter complexidade O(n log n) no pior caso.

17. **Encontrar o k-ésimo maior elemento**  
    Dada uma lista `A` contendo `n` inteiros, projete um algoritmo que retorne o k-ésimo maior elemento da lista. O algoritmo deve ter complexidade O(n) no pior caso.

18. **Ordenação por Heap**

Dada uma lista A contendo n inteiros, projete um algoritmo que ordene a lista utilizando o algoritmo de ordenação por heap (heap sort). O algoritmo deve ter complexidade O(n log n) no pior caso.

19. **Busca Binária em HashTable**

Dada uma HashTable contendo n inteiros, projete um algoritmo que realize uma busca binária em todos os elementos da HashTable para encontrar um valor específico. O algoritmo deve ter complexidade O(n log n) no pior caso.

20. **Seleção do k-ésimo menor elemento**

Dada uma lista A contendo n inteiros e um valor k, projete um algoritmo para encontrar o k-ésimo menor elemento na lista usando o algoritmo de seleção (por exemplo, o algoritmo de seleção de Quickselect). O algoritmo deve ter complexidade O(n) no pior caso.

21. **Algoritmo Gulosos para Atividades**

Dada uma lista de atividades, onde cada atividade é representada por um par de inteiros (start, end) indicando o tempo de início e o tempo de término da atividade, projete um algoritmo guloso que selecione o máximo número de atividades que podem ser realizadas sem sobreposição de horários. O algoritmo deve ter complexidade O(n log n) no pior caso.

22. **Busca Linear**

Dada uma lista A contendo n inteiros e um valor x, projete um algoritmo que encontre o índice de x na lista utilizando busca linear. O algoritmo deve ter complexidade O(n) no pior caso.

23. **Ordenação por Contagem**

Dada uma lista A de n inteiros que variam de 0 a k, projete um algoritmo que ordene a lista usando o algoritmo de ordenação por contagem (counting sort). O algoritmo deve ter complexidade O(n + k) no pior caso.

24. **Hashing com Encadeamento**

Dada uma HashTable com encadeamento para lidar com colisões, projete um algoritmo que insira e busque elementos na HashTable. O algoritmo de busca deve ter complexidade O(1) no caso médio.

25. **Ordenação por Inserção**

Dada uma lista A contendo n inteiros, projete um algoritmo que ordene a lista utilizando o algoritmo de ordenação por inserção (insertion sort). O algoritmo deve ter complexidade O(n^2) no pior caso.

26. **Ordenação por Shell**

Dada uma lista A contendo n inteiros, projete um algoritmo que ordene a lista utilizando o algoritmo de ordenação por Shell (shell sort). O algoritmo deve ter complexidade O(n^(3/2)) no pior caso.
