"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    My care is loss of care with old care done.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""


def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    #  TUTAJ PODAJ ROZWIĄZANIE ZADANIA

    wynik = []
    for query in queries:
        count_list = []
        document_list = []
        for number, document in enumerate(documents, 0):
            count = document.lower().count(query.lower())
            if count > 0:
                document_list.append(number)
                count_list.append(count)
        sorted_count_list = list(sorted(count_list, reverse=True))
        sorted_document_list = []
        for value1 in sorted_count_list:
            for nr, value2 in enumerate(count_list, 0):
                if value1 == value2:
                    if document_list[nr] not in sorted_document_list:
                        sorted_document_list.append(document_list[nr])
                        break
        wynik.append(sorted_document_list)

    # return [[]] - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)

    return wynik


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)