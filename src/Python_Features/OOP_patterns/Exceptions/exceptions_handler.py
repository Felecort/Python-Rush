print(issubclass(KeyError, LookupError))

while True:
    try:
        x = int(input("input value "))
        # break
    except ValueError:
        print("Uncorrect value")
    except KeyboardInterrupt:
        print("Exit...")
        break
    # Несколько исключений
    except (ValueError, KeyError):
        break
    # Никаких исключений
    else:
        print("No errors")
    # Выполняется всегда. Вообще всегда
    finally:
        print("Finally многолетний дебил")
