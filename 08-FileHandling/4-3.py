#Należy pamiętać, że niektóre operacje na plikach mogą spowodować zatrzymanie działania programu
#(np. brak pliku o podanej nazwie na dysku).
#Aby temu zapobiec, można użyć bloku try-except do obsługi wyjątków, czyli błędów,
# które mogą wystąpić podczas wykonywania programu.
# Wyjątki mogą wystąpić na przykład podczas próby dzielenia przez zero,
# dostępu do nieistniejącego pliku lub przetwarzania danych w niewłaściwym formacie.

#Idea bloku try-except polega na umieszczeniu kodu, który może spowodować błąd, wewnątrz bloku try,
# a jeśli wystąpi błąd, blok except go obsłuży, nie powodując awarii programu.

try:
   # code that may raise exceptions
except ExceptionType:
   # code to handle the exception


 Program read_file.py próbuje wydrukować zawartość pliku, którego nie ma na dysku.
 Przeczytaj zawartość programu. Następnie uruchom program i zobacz, co się stanie.
 Jak widać, program zatrzymuje się po wystąpieniu błędu (próba otwarcia nieistniejącego pliku).

Następnie sprawdź zawartość programu read_file_try_except.py,
który otwiera i odczytuje zawartość pliku w bloku try-except.
 Na koniec uruchom program.
 Jak widać, nawet po wystąpieniu błędu (próba otwarcia nieistniejącego pliku), program kontynuuje działanie.  