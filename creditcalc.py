import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["diff", "annuity"])
parser.add_argument("-py", "--payment")
parser.add_argument("-pr", "--principal")
parser.add_argument("-pd", "--periods")
parser.add_argument("-i", "--interest")
args = parser.parse_args()
alist = [args.type, args.principal, args.periods, args.interest, args.payment]

if bool((len(alist) < 4) and (args.interest is None) and (any(alist) < 0) and (args.type != "annuity" and "diff")) == True:
    print("Incorrect Parameters")

elif args.interest is None:
    print("Incorrect Parameters")
    

elif args.type == "diff":
    if args.payment is None:
        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)
        m = [x for x in range(1, n + 1)]
        total = 0

        for x in m:
            dm = math.ceil((p / n) + (i * (p - ((p * (x - 1)) / n))))
            print(f"Month {x}: payment is {dm}")
            total += dm
        overpayment = total - p
        print(f"Overpayment = {overpayment}")

elif args.type == "annuity":
     i = float(args.interest) / (12 * 100)

     if args.payment is None:
        p = int(args.principal)
        n = int(args.periods)
        c = math.pow((1 + i), n)

        a = math.ceil(p * ((i * c) / (c - 1)))

        print(f"Your annuity payment = {a}!")
        overpayment = n * a - p
        print(f"Overpayment = {overpayment}")

     if args.principal is None:
        n = int(args.periods)
        c = math.pow((1 + i), n)
        payment = int(args.payment)
        loan = int(payment / ((i * c) / (c - 1)))
        print(f"Your loan principal = {loan}!")
        overpayment = payment * n - loan
        print(f"Overpayment = {overpayment}")
     if args.periods is None:
        p = int(args.principal)
        payment = int(args.payment)

        n = math.log((payment / (payment - i * p)), 1 + i)
        n = math.ceil(n)
        years = math.floor(n / 12)
        months = int(((n / 12) - years) * 12)
        if years == 0:
            if months == 1:
                print(f"It will take 1 month to repay this loan!")
            else:
                print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")

        overpayment = payment * n - p
        print(f"Overpayment = {overpayment}")
