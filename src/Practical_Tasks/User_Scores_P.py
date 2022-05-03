
def main():
    path = "your path"
    more_my_res = 0
    less_my_res = 0
    MY_SCORE = 250
    
    with open(path, "r", encoding="UTF-8") as file:
        data = file.read().split()
        for user_score in data:
            if user_score.isdigit():
                if MY_SCORE < int(user_score) <= 300:
                    more_my_res += 1
                elif 100 < int(user_score) <= MY_SCORE:
                    less_my_res += 1
    better_result_persent = more_my_res / (more_my_res + less_my_res)
    print(more_my_res)
    print(less_my_res)
    print(f"Лучше: {better_result_persent * 100:.1f}%")


if __name__ == "__main__":
    main()
