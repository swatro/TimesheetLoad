import os


def lambda_handler(event, context):
    what_to_print = "hello world"
    how_many_times = 5

    print(f"Stacey is awesome!.")
    for i in range(0, how_many_times):
        print(f"what_to_print: {what_to_print}.")
    return what_to_print