# mortgage.py
#
# Exercise 1.7
pricipal = 500000.0
rate = 0.05
payment = 2684.11
total = 0
mouth = 0
start = 60
end = 108
while pricipal > 0:
    mouth += 1
    if mouth >= start and mouth <= end:
        pricipal = pricipal * (1+rate/12) - payment - 1000
        total += payment + 1000
    else:
        pricipal = pricipal * (1+rate/12) - payment
        total += payment

    print(round(total, 2), mouth)