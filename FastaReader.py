import os


class Seq:
    """
    Класс для хранения биологической последовательности (белка или нуклеиновой кислоты).
    """

    def __init__(self, header: str, sequence: str):
        self.header = header.strip()
        # Убираем пробелы и переводим в верхний регистр для удобства анализа
        self.sequence = "".join(sequence.split()).upper()

    def __len__(self) -> int:
        """Возвращает длину последовательности."""
        return len(self.sequence)

    def __str__(self) -> str:
        """Красивое строковое представление в формате FASTA."""
        # Разбиваем последовательность на строки по 60 символов (стандарт FASTA)
        seq_lines = [self.sequence[i:i + 60] for i in range(0, len(self.sequence), 60)]
        return f">{self.header}\n" + "\n".join(seq_lines)


    def get_alphabet_type(self) -> str:
        """
        Определяет тип последовательности: 'Nucleotide' (нуклеотидная) или 'Protein' (белковая).
        Нуклеотиды: A, T, G, C, U, N (и некоторые вырожденные, но ограничимся основными).
        """
        seq_set = set(self.sequence)
        nucleotide_chars = set("ATGCUN")

        if seq_set.issubset(nucleotide_chars):
            return "Nucleotide (ДНК/РНК)"
        else:
            return "Protein (Белок)"


class FastaReader:
    """
    Класс для чтения файлов формата FASTA.
    Использует генераторы для эффективной работы с большими файлами.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def _validate_file(self):
        """Проверяет соответствие файла формату FASTA."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Файл {self.filepath} не найден.")

        with open(self.filepath, 'r') as f:
            first_line = f.readline().strip()
            if not first_line.startswith('>'):
                raise ValueError("Ошибка формата: файл FASTA должен начинаться с символа '>'")

    def read_records(self):
        """
        Генератор, который читает файл по записям и возвращает объекты класса Seq.
        Благодаря yield, файл не загружается в память целиком.
        """
        self._validate_file()

        header = None
        seq_parts = []

        with open(self.filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Пропускаем пустые строки

                if line.startswith('>'):
                    # Если мы уже прочитали предыдущую последовательность, возвращаем её
                    if header is not None:
                        yield Seq(header, "".join(seq_parts))

                    # Начинаем новую запись
                    header = line[1:]  # Отрезаем символ '>'
                    seq_parts = []
                else:
                    if header is None:
                        raise ValueError("Ошибка формата: последовательность найдена до заголовка '>'")
                    seq_parts.append(line)

            # Не забываем вернуть последнюю последовательность в файле
            if header is not None:
                yield Seq(header, "".join(seq_parts))








