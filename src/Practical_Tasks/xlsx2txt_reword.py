from datetime import date
import pandas as pd


def get_data(path):
    data = pd.read_excel(path, header=2, usecols="B,C")
    e_words = data["English"].to_numpy()
    r_words = data["Russian"].to_numpy()
    return e_words, r_words


def parse_data(e_words, r_words):
    arr = []
    arr_append = arr.append
    for i in range(len(e_words)):
        arr_append(f'"{e_words[i]}";"{r_words[i]}"\n')
    return arr


def write_data(arr, path):
    with open(path, "w", encoding="utf8") as f:
        for line in arr:
            f.write(line)


def main():
    GENERAL_PARTH = "./data"
    parth_2_xlsx_file = f"{GENERAL_PARTH}/reword.xlsx"
    parth_2_txt_file = f"{GENERAL_PARTH}/reword_{date.today()}.txt"

    e_words, r_words = get_data(parth_2_xlsx_file)
    data = parse_data(e_words, r_words)
    write_data(data, parth_2_txt_file) 


if __name__ == "__main__":
    main()
