n = int(input())
tramposo = False
if n < 0:
    tramposo = True
else:
    if n < 100 and n%3 == 0 and n%2 != 0:
        tramposo = True
    elif n >= 100 and n%10 == 1:
        tramposo = True
if tramposo:
    print("Es tramposo")
else:
    print("No es tramposo")
