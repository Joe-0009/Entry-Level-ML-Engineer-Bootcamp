from time import sleep
from time import time


def ft_progress(lst):
    start_time = time()
    total = len(lst)

    for i, item in enumerate(lst, 1):
        elapsed_time = time() - start_time
        progress = i / total

        if elapsed_time > 0:
            speed = i / elapsed_time
            eta = (total - i) / speed if speed > 0 else 0
        else:
            eta = 0

        bar_length = 100
        filled_part = int(progress * bar_length)
        bar = '=' * filled_part + '>' + ' ' * (bar_length - filled_part)

        output = (
            f"\rETA: {eta:5.2f}s [{progress:3.0}%] "
            f"[{bar}] {i}/{total} | "
            f"elapsed time {elapsed_time:.2f}s"
        )

        print(output, end="", flush=True)

        yield item
