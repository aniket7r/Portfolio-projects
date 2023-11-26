import time

sample_test = "Typing is the process of writing or inputting text by pressing keys on a typewriter, computer keyboard, mobile phone, or calculator. It can be distinguished from other means of text input, such as handwriting and speech recognition. Text can be in the form of letters, numbers and other symbols. The world's first typist was Lillian Sholes from Wisconsin in the United States, the daughter of Christopher Sholes, who invented the first practical typewriter"


ready = input("are you ready? y/n")
if ready == "y":
    start_time = time.time()
    input_text = input()
    time_taken = time.time() - start_time
    print(time_taken)


def test_results():
    correct_words = 0
    for n in len(sample_test.split(" ")):
        if sample_test.split(" ")[n] == input_text.split(" ")[n]:
            correct_words+=1
    

        
