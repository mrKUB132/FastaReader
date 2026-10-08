import FastaReader
def main():

    # Создаем тестовый файл
    fasta_file = r"C:\Users\bogda\PycharmProjects\PythonProject1\Задачи_08_09_26\uniprot_sprot.fasta"

    reader = FastaReader.FastaReader(fasta_file)


    for seq_record in reader.read_records():
        print(f"Заголовок: {seq_record.header}")
        print(f"Длина: {len(seq_record)}")
        print(f"Тип алфавита: {seq_record.get_alphabet_type()}")



if __name__ == "__main__":
    main()