
OneToNine = {1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine"}
TenToNineteen = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fixteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}
Tens = {
    2: "Twenty",
    3: "Thirty",
    4: "Fourty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"


}
overall = 119  # Number here
FirstDigit = int(overall / 1000)
if FirstDigit > 0:
    print('%s Thousand ' % OneToNine[FirstDigit], end="")
SecondDigit = int(overall % 1000 / 100)
if SecondDigit > 0:
    print('%s Hundred ' % OneToNine[SecondDigit], end="")
ThirdDigit = int(overall % 100 / 10)
if ThirdDigit > 1:
    print(Tens[ThirdDigit], end="")
elif ThirdDigit == 1:
    print(TenToNineteen[overall % 100])
    raise SystemExit
ForthDigit = int(overall % 10)
if ForthDigit > 0:
    `
    print(OneToNine[ForthDigit])
