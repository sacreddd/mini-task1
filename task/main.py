import time


def main():
    bricks_count = format_input()
    triangles_count = 0
    count = 1
    last_side_length = 0
    start_time = time.time()
    print(start_time)
    for i in range(bricks_count):
        pause = time.time()
        side_length = int(input())
        pause_end = time.time()
        start_time += pause_end - pause
        if last_side_length == side_length:
            count += 1
            if count == 3:
                triangles_count += 1
                count = 0
        else:
            count = 1
            last_side_length = side_length
    print(start_time)
    print(time.time())
    print(triangles_count, "\n", (time.time() - start_time))


def format_input(tyr=input()):
    if tyr.isdigit():
        return int(tyr)
    else:
        print("это не число")


if __name__ == "__main__":
    main()
