import time
while True:
    print("Begin typing!\n")
    t0 = time.time() #start time
    inputText = str(input())
    t1 = time.time() #stop time  
    word_count = len(inputText.split())
    timeTaken = t1 - t0
    wordPM = (word_count/timeTaken*60)
    print ("Word typed:",word_count,"words")
    print ("Time taken:",timeTaken,"seconds")
    print ("Word per minute:",round(wordPM,3),"wpm")
    input("Press any key to start again...")
